"""Simple script to test connection to Redis and print an existing key."""
from redis import StrictRedis
import os

redis = StrictRedis(host=os.environ.get("REDIS_HOST", "localhost"),
                    port=os.environ.get("REDIS_PORT", 6379),
                    db=0)

a = redis.get("hello")
print type(a)

