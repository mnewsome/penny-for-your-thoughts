from django.test                  import TestCase, Client, RequestFactory
from django.core.urlresolvers     import reverse

from nosql_backend                import RedisWrapper
from tests.helpers.user_helper    import create_user
from tests.helpers.thought_helper import create_locked_thoughts
from thoughts                     import repository as thought_repository
import penny_for_your_thoughts.views as view

factory = RequestFactory()

INDEX_VIEW = 'penny_for_your_thoughts.views.index'
LOGIN_VIEW = 'penny_for_your_thoughts.views.login_user'
LOGOUT_VIEW = 'penny_for_your_thoughts.views.logout_user'

def create_index_post_request(user):
  return factory.post(reverse(INDEX_VIEW),
                              {'text': 'some post that I just made', 'user': user.id})

def create_login_post_request(username, password):
  return factory.post(reverse(LOGIN_VIEW), {'username': username, 'password': password})

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.index_response = self.client.get(reverse(INDEX_VIEW))

        self.test_user = create_user()
        create_locked_thoughts(10, self.test_user)

        self.index_post_request = create_index_post_request(self.test_user)

        self.redis_store = RedisWrapper(db=1)
        view.redis_store = self.redis_store

    def tearDown(self):
        self.redis_store.reset_unlocked_thought_pool()

    def test_index_view_get_request(self):
        self.assertEqual(self.index_response.status_code, 200)

    def test_index_view_context(self):
        self.assertTrue('auth_form' in self.index_response.context)
        self.assertTrue('locked_thought_count' in self.index_response.context)
        self.assertTrue('unlocked_thought_count' in self.index_response.context)
        self.assertTrue('next_locked_thought' in self.index_response.context)
        self.assertTrue('thought_form' in self.index_response.context)
        self.assertTrue('total_dollars_donated' in self.index_response.context)
        self.assertTrue('key' in self.index_response.context)

    def test_index_view_template(self):
        self.assertTemplateUsed('index.html')

    def test_index_view_decrements_thought_pool_when_thought_created(self):
        self.redis_store.increment_unlocked_thought_pool(10)
        view.index(self.index_post_request)
        self.assertEqual(9, self.redis_store.unlocked_thought_pool_value())

    def test_index_view_unlocks_thoughts_when_there_is_room_in_the_pool(self):
        self.redis_store.increment_unlocked_thought_pool(15)
        view.index(self.index_post_request)
        self.assertEqual(0, thought_repository.locked_thought_count())

    def test_login(self):
        response = self.client.post(reverse(LOGIN_VIEW), {'username': self.test_user.username, 'password': self.test_user.password})
        self.assertTrue(response.status_code, 302)

    def test_logout(self):
        response = self.client.get(reverse(LOGOUT_VIEW))
        self.assertTrue(response.status_code, 302)
