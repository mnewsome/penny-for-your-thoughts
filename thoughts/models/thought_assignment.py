from django.db import models

from thoughts.models import Thought
from payments.models import Payment

class ThoughtAssignment(models.Model):
  payments = models.ManyToManyField(Payment)
  thought = models.ForeignKey(Thought, unique=True)

  def __unicode__(self):
    try:
      payment_pk = self.payments.all().first().pk
    except AttributeError:
      payment_pk = "No Payment Assigned"

    return "Unlocked thought id: {0} by Payment id: {1}".format(self.thought.pk,
                                                   payment_pk)

  @classmethod
  def number_thoughts_assigned_to_payment(cls, payment_pk):
    return ThoughtAssignment.objects.filter(payments__pk=payment_pk).count()
