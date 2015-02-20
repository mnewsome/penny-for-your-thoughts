from django.db import models

from thoughts.models import Thought
from payments.models import Payment

class ThoughtAssignment(models.Model):
  payments = models.ManyToManyField(Payment)
  thought = models.ForeignKey(Thought, unique=True)

  def __unicode__(self):
    return "Unlocked thought id: {0} by {1}".format(self.thought.pk,
                                                    self.payments.all())
