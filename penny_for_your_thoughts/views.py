from os import environ as env
from django.shortcuts import render, redirect

from thoughts.forms import ThoughtForm
from thoughts.models import Thought

import stripe

stripe_keys = dict(
    secret_key=env.get('STRIPE_TEST_SECRET_KEY'),
    publishable_key=env.get('STRIPE_TEST_PUB_KEY')
    )

stripe.api_key = stripe_keys['secret_key']

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

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.POST['stripeToken']
        )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
        )

  return redirect('penny_for_your_thoughts.views.index')

def get_thought_form(request):
  if request.method == 'POST':
    thought_form = ThoughtForm(request.POST)
    if thought_form.is_valid():
      thought_form.save()
  else:
    thought_form = ThoughtForm(initial={'user': request.user})

  return thought_form
