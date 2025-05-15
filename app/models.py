from sqlalchemy import Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, nullable=False)
    platform = Column(String, nullable=False)
    hotel_name = Column(String, nullable=False)
    rating = Column(Float)
    review_date = Column(String)
    reviewer_info = Column(JSON)
    review_text = Column(String)
    metadata = Column(JSON)

class ProcessedFile(Base):
    __tablename__ = "processed_files"
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, unique=True, nullable=False)
    processed_at = Column(DateTime, default=datetime.utcnow, nullable=False)
