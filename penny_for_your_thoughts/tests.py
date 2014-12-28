from django.test import TestCase, Client
from django.core.urlresolvers import reverse

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
