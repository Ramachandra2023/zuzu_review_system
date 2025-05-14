import boto3
from config import Config

s3 = boto3.client('s3',
                  aws_access_key_id=Config.AWS_ACCESS_KEY,
                  aws_secret_access_key=Config.AWS_SECRET_KEY)

def list_review_files():
    response = s3.list_objects_v2(Bucket=Config.AWS_BUCKET_NAME, Prefix=Config.S3_PREFIX)
    return [obj['Key'] for obj in response.get('Contents', [])]

def download_file(key):
    response = s3.get_object(Bucket=Config.AWS_BUCKET_NAME, Key=key)
    return response['Body'].iter_lines()
