from django.core.urlresolvers import reverse
from django.test              import TestCase, RequestFactory

from accounts.interactor          import Interactor
from tests.helpers.user_helper    import create_general_user

ACCOUNT_VIEW = 'accounts.views.index'

class InteractorSpy(Interactor):
	def _donation_amount(self, user):
		return 500

class InteractorTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.request = self.factory.get(reverse(ACCOUNT_VIEW))
		self.test_user = create_general_user()
		self.request.user = self.test_user

	def test_presenter(self):
		interactor_spy = InteractorSpy(self.request)

		self.assertTrue('general_user' in interactor_spy.presenter())
		self.assertTrue('thoughts' in interactor_spy.presenter())
		self.assertTrue('donation_amount' in interactor_spy.presenter())
