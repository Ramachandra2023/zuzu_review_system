import pytest
from app.processor import parse_review

def test_parse_valid_review():
    line = '''{
        "hotelId": 10984,
        "platform": "Agoda",
        "hotelName": "Oscar Saigon Hotel",
        "comment": {
            "rating": 6.4,
            "reviewDate": "2025-04-10T05:37:00+07:00",
            "reviewerInfo": {"countryName": "India"},
            "reviewComments": "Nice stay."
        }
    }'''
    review = parse_review(line)
    assert review is not None
    assert review.hotel_id == 10984
    assert review.hotel_name == "Oscar Saigon Hotel"
    assert review.rating == 6.4

def test_parse_invalid_review_missing_fields():
    line = '''{
        "hotelId": 1234,
        "platform": "Agoda"
    }'''
    review = parse_review(line)
    assert review is None

def test_parse_malformed_json():
    line = '{hotelId: 10984,'
    review = parse_review(line)
    assert review is None
