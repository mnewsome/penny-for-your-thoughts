from django.db import models
from django.contrib.auth.models import User

class Thought(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_locked = models.BooleanField(default=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return """Thought ID: {0}
              Created: {1}
              Updated: {2}
              Locked?: {3}
              created by user: {4}""".format(self.pk,
                                             self.date_created,
                                             self.date_updated,
                                             self.is_locked,
                                             self.user
                                             )

    def save(self, pool_size=0, *args, **kwargs):
        if Thought._ready_to_unlock(pool_size):
            self.is_locked = False
            super (Thought, self).save(*args, **kwargs)
        else:
            super(Thought, self).save(*args, **kwargs)

    @classmethod
    def _ready_to_unlock(cls, pool_size):
        return True if pool_size > 0 else False
