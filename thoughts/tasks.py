from __future__ import absolute_import

from celery import shared_task

from thoughts.models import Thought

@shared_task
def unlock_thoughts(pool_size):
  return Thought.unlock_thoughts(pool_size)
