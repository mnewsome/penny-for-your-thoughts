from django.db.models import Sum

from payments.models import Payment

def donation_amount_by_user(user):
	payments = Payment.objects.filter(user=user).aggregate(Sum('amount'))
	return int(payments['amount__sum'] * .01)

def total_dollars_donated():
	amount_in_cents = Payment.objects.aggregate(Sum('amount'))['amount__sum']
	return amount_in_cents / 100 if amount_in_cents is not None else 0

def save(user, customer_id, amount):
	Payment(user=user, stripe_customer_id=customer_id, amount=amount).save()
