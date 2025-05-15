import pika, json
from db import save_review
from redis import Redis

redis_client = Redis(host='redis', port=6379)

def callback(ch, method, properties, body):
    review_data = json.loads(body)
    save_review(review_data)  # Save to DB
    cache_key = f"review:{review_data['comment']['hotelReviewId']}"
    redis_client.setex(cache_key, 3600, json.dumps(review_data))  # 1 hour TTL

def consume():
    conn = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = conn.channel()
    channel.queue_declare(queue='review_queue')
    channel.basic_consume(queue='review_queue', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages.')
    channel.start_consuming()

if __name__ == "__main__":
    consume()
