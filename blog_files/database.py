from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_PATH = 'sqlite:///./blog.db'

engine = create_engine(DATABASE_PATH, connect_args={"check_same_thread":False})

Base = declarative_base()

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()