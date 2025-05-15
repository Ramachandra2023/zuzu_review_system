import pytest

@pytest.fixture(scope="session")
def sample_review():
    return {
        "hotelId": 12345,
        "platform": "Booking.com",
        "hotelName": "Sample Hotel",
        "comment": {
            "hotelReviewId": 999999999,
            "rating": 8.5,
            "reviewDate": "2025-05-01T12:00:00+00:00",
            "reviewerInfo": {"countryName": "USA"},
            "reviewComments": "Excellent service!"
        }
    }
