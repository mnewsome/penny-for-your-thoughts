from django.db.models import Sum

from payments.models import Payment

def donation_amount_by_user(user):
	payments = Payment.objects.filter(user=user).aggregate(Sum('amount'))
	return int(payments['amount__sum'] * .01)
