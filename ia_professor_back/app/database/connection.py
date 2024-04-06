from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_MODE = config('TEST_MODE', default=False, cast=bool)
DB_URL = config('DB_URL', default='sqlite:///db.sqlite3')

engine = create_engine(DB_URL, echo=TEST_MODE,
    pool_pre_ping=True)
Session = sessionmaker(bind=engine)