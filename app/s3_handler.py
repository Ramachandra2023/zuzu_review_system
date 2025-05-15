import boto3
from app.config import Config

# Initialize S3 client with AWS credentials from Config
s3 = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY,
    aws_secret_access_key=Config.AWS_SECRET_KEY
)

def list_review_files():
    """
    Lists all review files under the specified S3 prefix.

    Returns:
        List[str]: List of S3 object keys.
    """
    response = s3.list_objects_v2(Bucket=Config.AWS_BUCKET_NAME, Prefix=Config.S3_PREFIX)
    if 'Contents' not in response:
        return []
    return [obj['Key'] for obj in response['Contents']]

def download_file(key):
    """
    Downloads a file from S3 and returns an iterator over its lines.

    Args:
        key (str): The S3 object key.

    Returns:
        Iterator[str]: An iterator over lines of the file content.
    """
    response = s3.get_object(Bucket=Config.AWS_BUCKET_NAME, Key=key)
    # The body is a StreamingBody, decode bytes to string lines
    return (line.decode('utf-8') for line in response['Body'].iter_lines())
