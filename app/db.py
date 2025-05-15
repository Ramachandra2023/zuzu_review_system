from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Review, ProcessedFile
from app.config import Config

# Create SQLAlchemy engine and session factory
engine = create_engine(Config.DB_URI)
Session = sessionmaker(bind=engine)

def init_db():
    """
    Initialize the database tables.
    """
    Base.metadata.create_all(engine)

def save_review(review_data):
    """
    Save a single review dict to the database as a Review ORM object.
    """
    session = Session()
    try:
        review = Review(
            hotel_id=review_data.get("hotelId"),
            platform=review_data.get("platform"),
            hotel_name=review_data.get("hotelName"),
            rating=review_data["comment"].get("rating"),
            review_date=review_data["comment"].get("reviewDate"),
            reviewer_info=review_data["comment"].get("reviewerInfo"),
            review_text=review_data["comment"].get("reviewComments"),
            metadata=review_data
        )
        session.add(review)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"[DB ERROR] Failed to save review: {e}")
    finally:
        session.close()

def has_been_processed(filename):
    """
    Check if a file has been processed already (idempotency).
    """
    session = Session()
    try:
        result = session.query(ProcessedFile).filter_by(filename=filename).first()
        return result is not None
    except Exception as e:
        print(f"[DB ERROR] Failed to check processed file: {e}")
        return False
    finally:
        session.close()

def mark_as_processed(filename):
    """
    Mark a file as processed to avoid reprocessing.
    """
    session = Session()
    try:
        processed_file = ProcessedFile(filename=filename)
        session.add(processed_file)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"[DB ERROR] Failed to mark file as processed: {e}")
    finally:
        session.close()
