from penny_for_your_thoughts import settings
import stripe

stripe_keys = dict(
     secret_key=settings.STRIPE_SECRET_KEY,
     publishable_key=settings.STRIPE_PUBLISHABLE_KEY
     )

stripe.api_key = stripe_keys['secret_key']

class PaymentManager:

  def create_customer(self, email, card):
    return stripe.Customer.create(
        email=email,
        card=card,
        )

  def create_charge(self, customer, amount):
    return stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Donation'
        )
