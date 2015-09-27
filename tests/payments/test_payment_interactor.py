from django.test                  import TestCase, Client, RequestFactory
from django.core.urlresolvers     import reverse

from lib.payment_manager       import PaymentManager
from payments.interactor       import Interactor
from tests.helpers.user_helper import create_user


CHARGE_VIEW = 'payments.views.charge'

class PaymentManagerSpy(PaymentManager):
	create_customer_was_called = False
	create_charge_was_called = False

	def create_customer(self, email, card):
		PaymentManagerSpy.create_customer_was_called = True
		return MockCustomer()

	def create_charge(self, customer, card):
		PaymentManagerSpy.create_charge_was_called = True
		return None

class MockCustomer:
	id = "customer_id"

class InteractorSpy(Interactor):
	save_payment_was_called = False
	adjust_thought_pool_was_called = False
	unlock_thoughts_was_called = False

	def _save_payment(self, user, customer_id, amount):
		InteractorSpy.save_payment_was_called = True
		return None

	def get_payment_manager(self):
		return PaymentManagerSpy()

	def _unlock_thoughts(self, amount):
		InteractorSpy.unlock_thoughts_was_called = True
		return None

	def _adjust_thought_pool(self, thoughts_updated_count, payment_amount):
		InteractorSpy.adjust_thought_pool_was_called = True
		return None


def create_charge_post_request():
	return factory.post(reverse(CHARGE_VIEW),
	                    {'amount': '500', 'email': 'some@email.com', 'stripeToken':'someToken'})

factory = RequestFactory()

class PaymentInteractorTest(TestCase):
	def setUp(self):
		self.request = create_charge_post_request()

		test_user = create_user()
		self.request.user = test_user

		self.interactor = InteractorSpy(PaymentManagerSpy())

	def test_create_customer_on_payment_manager_gets_called(self):
		self.interactor.charge(self.request)
		self.assertTrue(PaymentManagerSpy.create_customer_was_called)

	def test_create_charge_on_payment_manager_gets_called(self):
		self.interactor.charge(self.request)
		self.assertTrue(PaymentManagerSpy.create_charge_was_called)

	def test_save_payment_gets_called(self):
		self.interactor.charge(self.request)
		self.assertTrue(InteractorSpy.save_payment_was_called)

	def test_thoughts_get_unlocked(self):
		self.interactor.charge(self.request)
		self.assertTrue(InteractorSpy.unlock_thoughts_was_called)

	def test_thought_pool_gets_adjusted(self):
		self.interactor.charge(self.request)
		self.assertTrue(InteractorSpy.adjust_thought_pool_was_called)
