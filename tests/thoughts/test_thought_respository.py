from django.test import TestCase

from tests.helpers.user_helper    import create_user
from tests.helpers.thought_helper import create_locked_thoughts, create_unlocked_thoughts
from thoughts                     import repository
from thoughts.models              import Thought

class ThoughtRepositoryTestCase(TestCase):
	def setUp(self):
		self.test_user = create_user()
		create_locked_thoughts(2, self.test_user)
		create_unlocked_thoughts(1, self.test_user)

	def test_get_thoughts(self):
		self.assertEqual(3, len(repository.get_thoughts(user=self.test_user)))

	def test_get_thoughts_with_limit(self):
		self.assertEqual(3, len(repository.get_thoughts(3, user=self.test_user)))

	def test_get_locked_thought_count(self):
		count = repository.locked_thought_count()
		self.assertEqual(count, 2)

	def test_get_unlocked_thought_count(self):
		count = repository.unlocked_thought_count()
		self.assertEqual(count, 1)

	def test_get_next_locked_thought(self):
		thought = repository.next_locked_thought()
		self.assertEqual(thought.text, "Thought 1")

	def test_thought_is_unlocked_by_default_if_there_was_room_in_the_pool(self):
		unlocked_pool_size = 10
		thought = Thought.objects.create(text="thought created when pool is greater than 0", user=self.test_user)
		thought.save(unlocked_pool_size)
		self.assertFalse(thought.is_locked)

	def test_unlocks_all_available_thoughts(self):
		unlocked_pool_size = 10
		repository.unlock_thoughts(unlocked_pool_size)
		self.assertEqual(repository.unlocked_thought_count(), 3)

	def test_unlocks_thoughts_based_on_pool_size(self):
		unlocked_pool_size = 1
		repository.unlock_thoughts(unlocked_pool_size)
		self.assertEqual(repository.unlocked_thought_count(), 2)

	def test_no_thoughts_were_unlocked(self):
		locked_thoughts = Thought.objects.filter(is_locked=True)
		Thought.objects.filter(pk__in=locked_thoughts).update(is_locked=False)

		unlocked_pool_size = 10
		self.assertEqual(0, repository.unlock_thoughts(unlocked_pool_size))
