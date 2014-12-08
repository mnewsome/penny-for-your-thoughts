from django.test import TestCase
from django.contrib.auth.models import User

from thoughts.models import Thought
from penny_for_your_thoughts import views

class ThoughtTestCase(TestCase):
  def setUp(self):
    test_user = User.objects.create_user('malcolm', 'malcolm@something.com', 'password')

    Thought.objects.create(text="Thought 1", user=test_user)
    Thought.objects.create(text="Thought 2", user=test_user)
    Thought.objects.create(text="Thought 3", user=test_user, is_locked=False)

  def test_get_locked_thought_count(self):
    count = Thought.locked_thought_count()
    self.assertEqual(count, 2)

  def test_get_unlocked_thought_count(self):
    count = Thought.unlocked_thought_count()
    self.assertEqual(count, 1)

  def test_get_next_locked_thought(self):
    thought = Thought.next_locked_thought()
    self.assertEqual(thought.text, "Thought 1")

  def test_ready_to_unlock(self):
    unlocked_pool_size = 100
    self.assertTrue(Thought.ready_to_unlock(unlocked_pool_size))

  def test_not_ready_to_unlock(self):
    unlocked_pool_size = 0
    self.assertFalse(Thought.ready_to_unlock(unlocked_pool_size))
