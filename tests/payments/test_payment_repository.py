from django.test import TestCase

from payments                     import repository
from tests.helpers.payment_helper import create_payment
from tests.helpers.user_helper    import create_user

class PaymentRepositoryTest(TestCase):
	def setUp(self):
		self.test_user = create_user()
		create_payment(self.test_user, 500)

	def test_donation_amount_by_user(self):
		self.assertEqual(5, repository.donation_amount_by_user(self.test_user))

	def test_retrieve_total_of_all_payments(self):
		self.assertEqual(5, repository.total_dollars_donated())
