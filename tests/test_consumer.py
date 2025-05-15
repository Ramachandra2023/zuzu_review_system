import json
import pytest
from unittest.mock import patch

from consumer.consumer import callback

@pytest.fixture
def valid_review():
    return {
        "hotelId": 10984,
        "platform": "Agoda",
        "hotelName": "Oscar Saigon Hotel",
        "comment": {
            "hotelReviewId": 948353737,
            "rating": 6.4,
            "reviewDate": "2025-04-10T05:37:00+07:00",
            "reviewerInfo": {"countryName": "India"},
            "reviewComments": "Great location, small room."
        }
    }

@patch("consumer.consumer.save_review")
@patch("consumer.consumer.cache_review")
def test_callback_success(mock_cache, mock_save, valid_review):
    # Simulate delivery from RabbitMQ
    message_body = json.dumps(valid_review).encode("utf-8")

    # Call the callback function directly
    callback(ch=None, method=None, properties=None, body=message_body)

    # Assert DB save and cache functions were called correctly
    mock_save.assert_called_once_with(valid_review)
    mock_cache.assert_called_once_with(valid_review["comment"]["hotelReviewId"], valid_review)
