from django.contrib.auth.models import User
from django.db.models           import Sum

from payments.models import Payment
from thoughts        import repository

class Interactor():
	def __init__(self, request):
		self.request = request

	def presenter(self):
		user = User.objects.get(username=self.request.user.username)
		thoughts = self._get_thoughts(user)

		context = dict(
			general_user    = user.generaluser,
			thoughts        = thoughts,
			donation_amount = self._donation_amount(user),
		)
		return context

	def _get_thoughts(self, user):
		return repository.get_thoughts(user=user)

	def _donation_amount(self, user):
		payments = Payment.objects.filter(user=user).aggregate(Sum('amount'))
		return int(payments['amount__sum'] * .01)
