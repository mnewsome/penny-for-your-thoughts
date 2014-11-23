from django.db import models

class Thought(models.Model):
  text = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  is_locked = models.BooleanField(default=True)

  def __unicode__(self):
    return self.text

  @classmethod
  def locked_thought_count(cls):
    return Thought.objects.filter(is_locked=True).count()

  @classmethod
  def next_locked_thought(cls):
    return Thought.objects.filter(is_locked=True).order_by('date_created').first()
