from django.test import TestCase

from tests.test_helpers import create_user
from payments.models import Payment

class TestPayments(TestCase):
  def setUp(self):
    test_user = create_user()

    Payment.objects.create(user=test_user, stripe_customer_id="some id", amount=500)
    Payment.objects.create(user=test_user, stripe_customer_id="some id", amount=1500)
    Payment.objects.create(user=test_user, stripe_customer_id="some id", amount=500)

  def test_retrieve_total_of_all_payments(self):
    self.assertEqual(2500, Payment.total_amount_donated())
