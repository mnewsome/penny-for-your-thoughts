from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from lib.payment_manager import PaymentManager
from tests.thoughts.helpers import *
from thoughts.models import Thought
from payments.models import Payment
import penny_for_your_thoughts.views as view

INDEX_VIEW = 'penny_for_your_thoughts.views.index'
CHARGE_VIEW = 'penny_for_your_thoughts.views.charge'

class PaymentManagerSpy(PaymentManager):
  def create_customer(self, email, card):
    return MockCustomer()

  def create_charge(self, customer, card):
    return None

class MockCustomer:
    id = "cust_id"

def create_post_request():
    factory = RequestFactory()
    view.get_payment_manager = PaymentManagerSpy
    return factory.post(reverse(CHARGE_VIEW),
                               {'stripeEmail': 'some@email.com', 'stripeToken':'someToken'})

class ViewsTest(TestCase):
  def setUp(self):
    self.client = Client()

    self.index_response = self.client.get(reverse(INDEX_VIEW))
    self.test_user = User.objects.create_user(username='malcolm', email='malcolm@newsome.com', password='password')
    create_locked_thoughts(10, self.test_user)

    self.post_request = create_post_request()
    self.post_request.user = self.test_user

  def test_index_view_response(self):
    self.assertEqual(self.index_response.status_code, 200)

  def test_index_view_context(self):
    self.assertTrue('locked_thought_count' in self.index_response.context)
    self.assertTrue('unlocked_thought_count' in self.index_response.context)
    self.assertTrue('next_locked_thought' in self.index_response.context)
    self.assertTrue('thought_form' in self.index_response.context)
    self.assertTrue('key' in self.index_response.context)

  def test_index_view_template(self):
    self.assertTemplateUsed('index.html')

  def test_charge_view_response(self):
    response = self.client.get(reverse(CHARGE_VIEW))
    self.assertEqual(response.status_code, 405)

  def test_charget_view_saves_payment(self):
    view.charge(self.post_request)
    self.assertEqual(1, Payment.objects.count())

  def test_charge_view_unlocks_thoughts(self):
    view.charge(self.post_request)
    self.assertEqual(10, Thought.unlocked_thought_count())
