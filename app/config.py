import os

class Config:
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    S3_PREFIX = os.getenv("S3_PREFIX", "reviews/")
    DB_URI = os.getenv("DB_URI", "postgresql://user:pass@db/reviews")
