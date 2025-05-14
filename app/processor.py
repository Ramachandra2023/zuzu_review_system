import json
from models import Review

REQUIRED_FIELDS = ["hotelId", "platform", "hotelName", "comment"]

def validate_review(data):
    return all(field in data for field in REQUIRED_FIELDS)

def parse_review(line):
    try:
        data = json.loads(line)
        if not validate_review(data):
            return None
        comment = data["comment"]
        return Review(
            hotel_id=data["hotelId"],
            platform=data["platform"],
            hotel_name=data["hotelName"],
            rating=comment.get("rating"),
            review_date=comment.get("reviewDate"),
            reviewer_info=comment.get("reviewerInfo"),
            review_text=comment.get("reviewComments"),
            metadata=data
        )
    except Exception:
        return None
