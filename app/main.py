from app.s3_handler import list_review_files, download_file
from app.processor import validate_review
from app.db import init_db, save_review, has_been_processed, mark_as_processed
import json

def run():
    # Initialize DB tables
    init_db()
    
    # List files in S3 bucket under the prefix
    files = list_review_files()
    
    for file_key in files:
        if has_been_processed(file_key):
            print(f"Skipping already processed file: {file_key}")
            continue

        print(f"Processing file: {file_key}")
        try:
            lines = download_file(file_key)
            for line in lines:
                try:
                    review_json = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Malformed JSON line skipped: {e}")
                    continue
                
                if validate_review(review_json):
                    save_review(review_json)
                else:
                    print("Invalid review data; skipping.")
            
            # Mark file as processed only after full successful pass
            mark_as_processed(file_key)
        except Exception as e:
            print(f"Error processing file {file_key}: {e}")

if __name__ == "__main__":
    run()
