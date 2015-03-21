from django.test import TestCase

from tests.helpers.user_helper import create_user
from tests.helpers.thought_helper import create_locked_thoughts
from tests.helpers.payment_helper import create_payment
from thoughts.models import Thought, ThoughtAssignment
from payments.models import Payment

class ThoughtAssignmentTestCase(TestCase):
  def setUp(self):
    test_user = create_user()
    create_locked_thoughts(10, test_user)
    donor = create_user(username='DonR', email='donor@donor.com')
    create_payment(donor, 500)

    self.thoughts = Thought.objects.all()
    self.payment = Payment.objects.order_by('date_created').first()

  def test_thoughts_are_assigned_to_the_user_who_made_the_payment(self):
    ThoughtAssignment.assign(self.payment, self.thoughts)
    self.assertEqual(10, ThoughtAssignment.objects.count())

  def test_assigned_thought_has_an_associated_payment(self):
    ThoughtAssignment.assign(self.payment, self.thoughts)
    self.assertEqual(ThoughtAssignment.objects.first().payments.first().pk, self.payment.pk)

  def test_number_of_thoughts_assigned_to_payment(self):
    ThoughtAssignment.assign(self.payment, self.thoughts)
    self.assertEqual(10, ThoughtAssignment.number_thoughts_assigned_to_payment(self.payment.pk))
