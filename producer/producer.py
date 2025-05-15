import pika, json
from s3_handler import list_review_files, download_file
from processor import validate_review

def send_to_queue(review_json):
    conn = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = conn.channel()
    channel.queue_declare(queue='review_queue')
    channel.basic_publish(exchange='',
                          routing_key='review_queue',
                          body=json.dumps(review_json))
    conn.close()

def run():
    files = list_review_files()
    for file_key in files:
        for line in download_file(file_key):
            review = json.loads(line)
            if validate_review(review):
                send_to_queue(review)

if __name__ == "__main__":
    run()
