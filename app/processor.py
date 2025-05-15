import json

# List of required top-level fields to consider a review valid
REQUIRED_FIELDS = ["hotelId", "platform", "hotelName", "comment"]

def validate_review(data):
    """
    Validates that the review JSON data contains required fields.

    Args:
        data (dict): Parsed JSON review line.

    Returns:
        bool: True if valid, False otherwise.
    """
    return all(field in data for field in REQUIRED_FIELDS)

def parse_review(line):
    """
    Parses a JSON line into a dict if valid.

    Args:
        line (str): A JSON string representing a review.

    Returns:
        dict or None: Parsed dict if valid, else None.
    """
    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        return None

    if validate_review(data):
        return data
    else:
        return None
