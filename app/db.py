from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from models import Base

engine = create_engine(Config.DB_URI)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def save_reviews(reviews):
    session = Session()
    for review in reviews:
        session.add(review)
    session.commit()
    session.close()
