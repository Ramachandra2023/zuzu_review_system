import os

class Config:
    # AWS S3 Config
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
    S3_PREFIX = os.getenv("S3_PREFIX", "reviews/")

    # Database
    DB_URI = os.getenv("DB_URI", "postgresql://user:password@localhost/review_db")

    # Redis
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

    # RabbitMQ
    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
    RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "review_queue")

    # General
    DEFAULT_CACHE_TTL = int(os.getenv("DEFAULT_CACHE_TTL", 3600))  # in seconds
