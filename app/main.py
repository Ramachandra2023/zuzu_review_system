from s3_handler import list_review_files, download_file
from processor import parse_review
from db import save_reviews, init_db


def run():
    init_db()
    files = list_review_files()
    for file_key in files:
        print(f"Processing {file_key}...")
        lines = download_file(file_key)
        reviews = []
        for line in lines:
            review = parse_review(line)
            if review:
                reviews.append(review)
        save_reviews(reviews)


if __name__ == "__main__":
    run()
