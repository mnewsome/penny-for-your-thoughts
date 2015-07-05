from nosql_backend       import RedisWrapper
from payments            import repository as payment_repository
from thoughts            import repository as thought_repository

redis_store = RedisWrapper()

class Interactor():

	def __init__(self, payment_manager):
		self.payment_manager = payment_manager

	def charge(self, request):
		if request.method == 'POST':
			amount = int(request.POST['amount'])
			email = request.POST['email']
			token = request.POST['stripeToken']

			customer = self.payment_manager.create_customer(email, token)
			self.payment_manager.create_charge(customer, amount)

			self._save_payment(request.user, customer.id, amount)
			updated_thought_count = self._unlock_thoughts(amount)
			self._adjust_thought_pool(updated_thought_count, amount)

		return None

	def _save_payment(self, user, customer_id, amount):
		payment_repository.save(user, customer_id, amount)
		return  None

	def _unlock_thoughts(self, amount):
		return thought_repository.unlock_thoughts(amount)

	def _adjust_thought_pool(self, thoughts_updated_count, payment_amount):
		if thoughts_updated_count < payment_amount:
			return redis_store.increment_unlocked_thought_pool(payment_amount - thoughts_updated_count)
