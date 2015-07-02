from django.test import TestCase

from tests.helpers.user_helper    import create_user
from tests.helpers.thought_helper import create_locked_thoughts
from thoughts                     import repository

class ThoughtRepositoryTestCase(TestCase):
    def setUp(self):
        self.test_user = create_user()
        create_locked_thoughts(5, self.test_user)

    def test_get_thoughts(self):
        self.assertEqual(5, len(repository.get_thoughts(user=self.test_user)))

    def test_get_thoughts_with_limit(self):
        self.assertEqual(3, len(repository.get_thoughts(3, user=self.test_user)))
