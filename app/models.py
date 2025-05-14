from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer)
    platform = Column(String)
    hotel_name = Column(String)
    rating = Column(Float)
    review_date = Column(String)
    reviewer_info = Column(JSON)
    review_text = Column(String)
    metadata = Column(JSON)

class ProcessedFile(Base):
    __tablename__ = "processed_files"
    id = Column(Integer, primary_key=True)
    filename = Column(String, unique=True, nullable=False)
    processed_at = Column(DateTime, default=datetime.utcnow)
