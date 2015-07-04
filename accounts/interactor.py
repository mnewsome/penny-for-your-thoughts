from django.contrib.auth.models import User

from payments        import repository as payment_repository
from thoughts        import repository as thought_repository

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
		return thought_repository.get_thoughts(user=user)

	def _donation_amount(self, user):
		return payment_repository.donation_amount_by_user(user)
