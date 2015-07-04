from django.test import TestCase

from payments                     import repository
from tests.helpers.payment_helper import create_payment
from tests.helpers.user_helper    import create_user

class PaymentRepositoryTest(TestCase):
	def test_donation_amount_by_user(self):
		test_user = create_user()
		create_payment(test_user, 500)
		self.assertEqual(5, repository.donation_amount_by_user(test_user))
