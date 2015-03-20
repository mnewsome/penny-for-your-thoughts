from payments.models import Payment
from thoughts.models import Thought, ThoughtAssignment

class ThoughtManager:
  def assign_thoughts(self, payment, thoughts):
    assignments = [ThoughtAssignment(thought=thought) for thought in thoughts]
    ThoughtAssignment.objects.bulk_create(assignments)
    saved_assigments = ThoughtAssignment.objects.all()[:len(assignments)]
    for assignment in saved_assigments:
      assignment.payments.add(payment)
