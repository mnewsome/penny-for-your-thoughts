from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from lib import payment_manager

from lib.payment_manager import stripe_keys, PaymentManager
from nosql_backend import RedisWrapper
from thoughts.forms import ThoughtForm
from thoughts.models import Thought
from payments.models import Payment


redis_store = RedisWrapper()

def index(request):
  if request.method == 'GET':
    thought_form = ThoughtForm(initial={'user': request.user})

  if request.method == 'POST':
    thought_form = ThoughtForm(request.POST)
    if thought_form.is_valid():
      thought_form.save()
      redis_store.decrement_unlocked_thought_pool(1)

  context = dict(
           locked_thought_count=Thought.locked_thought_count(),
           unlocked_thought_count=Thought.unlocked_thought_count(),
           next_locked_thought=Thought.next_locked_thought(),
           thought_form=thought_form,
           total_dollars_donated=Payment.total_dollars_donated(),
           key=stripe_keys['publishable_key'],
           )

  Thought.unlock_thoughts(redis_store.unlocked_thought_pool_value())
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

    Payment(user=request.user, stripe_customer_id=customer.id, amount=amount).save()
    updated_thought_count = Thought.unlock_thoughts(amount)
    adjust_thought_pool(updated_thought_count, amount)

  return redirect('penny_for_your_thoughts.views.index')

def unlock_thoughts():
  Thought.unlock_thoughts()

def get_payment_manager():
  return PaymentManager()

def adjust_thought_pool(thoughts_updated_count, payment_amount):
  if thoughts_updated_count < payment_amount:
    return redis_store.increment_unlocked_thought_pool(payment_amount - thoughts_updated_count)
