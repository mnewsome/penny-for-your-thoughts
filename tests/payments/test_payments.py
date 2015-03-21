from django.test import TestCase

from payments.models import Payment
from tests.helpers.user_helper import create_user
from tests.helpers.payment_helper import create_payment

class TestPayments(TestCase):
  def setUp(self):
    test_user = create_user()

    create_payment(test_user, 500)
    create_payment(test_user, 1500)
    create_payment(test_user, 500)

  def test_retrieve_total_of_all_payments(self):
    self.assertEqual(25, Payment.total_dollars_donated())
