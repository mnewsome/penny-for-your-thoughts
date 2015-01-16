from django.test import TestCase

from tests.test_helpers import create_user
from tests.thoughts.thought_helpers import create_locked_thoughts, create_unlocked_thoughts
from thoughts.models import Thought
from penny_for_your_thoughts import views

class ThoughtTestCase(TestCase):
  def setUp(self):
    self.test_user = create_user()
    create_locked_thoughts(2, self.test_user)
    create_unlocked_thoughts(1, self.test_user)

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

  def test_thought_is_unlocked_by_default_if_there_was_room_in_the_pool(self):
    unlocked_pool_size = 10
    thought = Thought.objects.create(text="thought created when pool is greater than 0", user=self.test_user)
    thought.save(unlocked_pool_size)
    self.assertFalse(thought.is_locked)

  def test_thought_worker_unlocks_all_available_thoughts(self):
    unlocked_pool_size = 10
    Thought.unlock_thoughts(unlocked_pool_size)
    self.assertEqual(Thought.unlocked_thought_count(), 3)

  def test_thought_worker_unlocks_thoughts_based_on_pool_size(self):
    unlocked_pool_size = 1
    Thought.unlock_thoughts(unlocked_pool_size)
    self.assertEqual(Thought.unlocked_thought_count(), 2)
