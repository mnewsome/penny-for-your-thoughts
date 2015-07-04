from django.contrib               import messages
from django.contrib.auth          import authenticate, login, logout
from django.contrib.auth.forms    import AuthenticationForm
from django.shortcuts             import render, redirect
from django.views.decorators.http import require_POST, require_GET

from lib.payment_manager import stripe_keys, PaymentManager
from nosql_backend       import RedisWrapper
from thoughts.forms      import ThoughtForm
from thoughts            import repository as thought_repository
from payments            import repository as payment_repository

redis_store = RedisWrapper()

@require_POST
def login_user(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('penny_for_your_thoughts.views.index')
        else:
            messages.error(request, 'This account is not active')
            return redirect('penny_for_your_thoughts.views.index')
    else:
        messages.error(request, 'Invalid username/password')
        return redirect('penny_for_your_thoughts.views.index')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('penny_for_your_thoughts.views.index')

def index(request):
    auth_form = AuthenticationForm(request)

    if request.method == 'GET':
        thought_form = ThoughtForm(initial={'user': request.user})

    if request.method == 'POST':
        thought_form = ThoughtForm(request.POST)
    if thought_form.is_valid():
        thought_form.save()
        redis_store.decrement_unlocked_thought_pool(1)

    context = dict(
            auth_form              = auth_form,
            locked_thought_count   = thought_repository.locked_thought_count(),
            unlocked_thought_count = thought_repository.unlocked_thought_count(),
            next_locked_thought    = thought_repository.next_locked_thought(),
            thought_form           = thought_form,
            total_dollars_donated  = payment_repository.total_dollars_donated(),
            key                    = stripe_keys['publishable_key'],
            )

    thought_repository.unlock_thoughts(redis_store.unlocked_thought_pool_value())
    return render(request, 'index.html', context)

@require_POST
def charge(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        email = request.POST['email']
        token = request.POST['stripeToken']

        payment_manager = get_payment_manager()
        customer = payment_manager.create_customer(email, token)
        payment_manager.create_charge(customer, amount)

        payment_repository.save(request.user, customer.id, amount)
        updated_thought_count = thought_repository.unlock_thoughts(amount)
        adjust_thought_pool(updated_thought_count, amount)

    return redirect('penny_for_your_thoughts.views.index')

def unlock_thoughts():
    thought_repository.unlock_thoughts()

def get_payment_manager():
    return PaymentManager()

def adjust_thought_pool(thoughts_updated_count, payment_amount):
    if thoughts_updated_count < payment_amount:
        return redis_store.increment_unlocked_thought_pool(payment_amount - thoughts_updated_count)
