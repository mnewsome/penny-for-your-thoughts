from django.core.urlresolvers import reverse
from django.test              import TestCase, Client, RequestFactory


import accounts.views as view
from tests.helpers.user_helper import create_general_user
from tests.helpers.payment_helper import create_payment

ACCOUNT_VIEW = 'accounts.views.index'

class AccountsViewsTest(TestCase):
  def setUp(self):
    self.client = Client()
    self.test_user = create_general_user()
    self.factory = RequestFactory()
    self.request = self.factory.get(reverse(ACCOUNT_VIEW))
    self.request.user = self.test_user
    create_payment(self.test_user, 500)

  def test_index_view_successful_when_user_is_logged_in(self):
    response = view.index(self.request)
    self.assertTrue(response.status_code, 200)
