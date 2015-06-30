from django.core.urlresolvers import reverse
from django.test              import TestCase, RequestFactory

from accounts.interactor          import Interactor
from tests.helpers.user_helper    import create_general_user
from tests.helpers.payment_helper import create_payment

ACCOUNT_VIEW = 'accounts.views.index'

class InteractorTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.request = self.factory.get(reverse(ACCOUNT_VIEW))
		self.test_user = create_general_user()
		self.request.user = self.test_user

	def test_presenter(self):
		interactor = Interactor(self.request)
		create_payment(self.test_user, 500)

		self.assertTrue('general_user' in interactor.presenter())
		self.assertTrue('thoughts' in interactor.presenter())
		self.assertTrue('donation_amount' in interactor.presenter())
