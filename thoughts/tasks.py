from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger

from thoughts.models import Thought

logger = get_task_logger(__name__)

@shared_task
def unlock_thoughts(pool_size):
  thoughts_unlocked = Thought.unlock_thoughts(pool_size)
  logger.info("{0} thoughts unlocked".format(thoughts_unlocked))
  return thoughts_unlocked
