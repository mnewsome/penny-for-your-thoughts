from penny_for_your_thoughts import settings

import redis

UNLOCKED_THOUGHT_POOL = 'unlocked_thought_pool'

class RedisWrapper:
  def __init__(self, host=settings.REDIS_HOST,
                     port=settings.REDIS_PORT,
                     db=settings.REDIS_DB):

    self.host = host
    self.port = port
    self.db   = db

    self.datastore = redis.StrictRedis(host=self.host,
                                       port=self.port,
                                       db=self.db)

  def increment_unlocked_thought_pool(self, value):
    return self.datastore.incrby(UNLOCKED_THOUGHT_POOL, value)

  def decrement_unlocked_thought_pool(self, value):
    return self.datastore.decr(UNLOCKED_THOUGHT_POOL, value)

  def unlocked_thought_pool_value(self):
    try:
      return int(self.datastore.get(UNLOCKED_THOUGHT_POOL))
    except TypeError:
      return 0

  def reset_unlocked_thought_pool(self):
    return self.datastore.set(UNLOCKED_THOUGHT_POOL, 0)
