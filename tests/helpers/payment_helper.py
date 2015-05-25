from payments.models import Payment

def create_payment(user, amount):
  Payment.objects.create(user=user, stripe_customer_id="some-id", amount=amount)
