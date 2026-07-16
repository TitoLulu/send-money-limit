from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:///wallet.db", future=True)
SessionLocal = sessionmaker(bind=engine, future=True)
