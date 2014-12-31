from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from lib.payment_manager import PaymentManager
from payments.models import Payment
import penny_for_your_thoughts.views as view

class PaymentManagerSpy(PaymentManager):
  def create_customer(self, email, card):
    return MockCustomer()

  def create_charge(self, customer, card):
    return None

class MockCustomer:
    id = "cust_id"

class ViewsTest(TestCase):
  def setUp(self):
    self.client = Client()
    self.index_response = self.client.get(reverse('penny_for_your_thoughts.views.index'))

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
    response = self.client.get(reverse('penny_for_your_thoughts.views.charge'))
    self.assertEqual(response.status_code, 302)

  def test_charget_view_saves_payment(self):
    factory = RequestFactory()
    view.get_payment_manager = PaymentManagerSpy

    request = factory.post(reverse('penny_for_your_thoughts.views.charge'),
                                  {'stripeEmail': 'some@email.com', 'stripeToken':'someToken'})
    user = User.objects.create_user(username='malcolm', email='malcolm@newsome.com', password='password')
    request.user = user

    view.charge(request)

    self.assertEqual(1, Payment.objects.count())
