from penny_for_your_thoughts import settings

import redis

datastore = redis.StrictRedis(host=settings.REDIS_HOST,
                              port=settings.REDIS_PORT,
                              db=settings.REDIS_DB)

UNLOCKED_THOUGHT_POOL = 'unlocked_thought_pool'

def increment_unlocked_thought_pool(value):
  return datastore.incrby(UNLOCKED_THOUGHT_POOL, value)

def decrement_unlocked_thought_pool(value):
  return datastore.decr(UNLOCKED_THOUGHT_POOL, value)

def unlocked_thought_pool_value():
  return int(datastore.get(UNLOCKED_THOUGHT_POOL))
