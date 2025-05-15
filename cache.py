import redis
import json
from app.config import Config

# Initialize Redis client
client = redis.Redis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    decode_responses=True  # ensures string return, not bytes
)

def cache_review(review_id, review_data, ttl=3600):
    """
    Cache the review JSON data with an optional time-to-live (default 1 hour).
    """
    key = f"review:{review_id}"
    try:
        client.setex(key, ttl, json.dumps(review_data))
    except Exception as e:
        print(f"[Redis Error] Failed to cache review {review_id}: {e}")

def get_cached_review(review_id):
    """
    Retrieve cached review JSON from Redis if available.
    """
    key = f"review:{review_id}"
    try:
        data = client.get(key)
        return json.loads(data) if data else None
    except Exception as e:
        print(f"[Redis Error] Failed to retrieve review {review_id}: {e}")
        return None
