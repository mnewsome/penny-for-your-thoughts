from django.test import TestCase, Client

from tests.helpers.user_helper import create_user
from tests.helpers.thought_helper import create_locked_thoughts
from thoughts.models import Thought

class ViewsTest(TestCase):
  def setUp(self):
    client = Client()
    test_user = create_user()
    create_locked_thoughts(10, test_user)
    thought_id = Thought.objects.all()[0].id
    self.response = client.get('/thought/{}/'.format(thought_id))

  def test_show_view_get_request(self):
    self.assertEqual(self.response.status_code, 200)

  def test_show_view_context(self):
    self.assertTrue('thought' in self.response.context)

  def test_show_view_template(self):
    self.assertTemplateUsed('thoughts/show.html')
