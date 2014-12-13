import redis
from os import environ as env

datastore = redis.StrictRedis(host=env.get('REDIS_DEV_HOST'), port=env.get('REDIS_DEV_PORT'), db=env.get('REDIS_DEV_DB'))

UNLOCKED_THOUGHT_POOL = 'unlocked_thought_pool'

def increment_unlocked_thought_pool(value):
  return datastore.incrby(UNLOCKED_THOUGHT_POOL, value)

def decrement_unlocked_thought_pool(value):
  return datastore.decr(UNLOCKED_THOUGHT_POOL, value)

def unlocked_thought_pool_value():
  return int(datastore.get(UNLOCKED_THOUGHT_POOL))
