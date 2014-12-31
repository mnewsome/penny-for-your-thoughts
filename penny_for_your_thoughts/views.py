from django.shortcuts import render, redirect

from lib.payment_manager import stripe_keys, PaymentManager
from thoughts.forms import ThoughtForm
from thoughts.models import Thought
from payments.models import Payment

def index(request):
  context = dict(
           locked_thought_count=Thought.locked_thought_count(),
           unlocked_thought_count=Thought.unlocked_thought_count(),
           next_locked_thought=Thought.next_locked_thought(),
           thought_form=get_thought_form(request),
           key=stripe_keys['publishable_key'],
           )

  return render(request, 'index.html', context)

def charge(request):
  if request.method == 'POST':
    amount = 500

    payment_manager = get_payment_manager()
    customer = payment_manager.create_customer(request.POST['stripeEmail'],
                                               request.POST['stripeToken'])
    payment_manager.create_charge(customer, amount)

    Payment(user=request.user, stripe_customer_id=customer.id, amount=amount).save()

  return redirect('penny_for_your_thoughts.views.index')

def get_payment_manager():
  return PaymentManager()

def get_thought_form(request):
  if request.method == 'POST':
    thought_form = ThoughtForm(request.POST)
    if thought_form.is_valid():
      thought_form.save()
  else:
    thought_form = ThoughtForm(initial={'user': request.user})

  return thought_form
