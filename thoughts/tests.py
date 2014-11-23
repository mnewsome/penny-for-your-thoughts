from django.test import TestCase

from thoughts.models import Thought
from penny_for_your_thoughts import views

class ThoughtTestCase(TestCase):
  def setUp(self):
    Thought.objects.create(text="Thought 1")
    Thought.objects.create(text="Thought 2")

  def test_get_locked_thought_count(self):
    count = Thought.locked_thought_count()
    self.assertEqual(count, 2)

  def test_get_next_locked_thought(self):
    thought = Thought.next_locked_thought()
    self.assertEqual(thought.text, "Thought 1")
