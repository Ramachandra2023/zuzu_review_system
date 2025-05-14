from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

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
