from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import os
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
#SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db

    finally:
        db.close()

print(SQLALCHEMY_DATABASE_URL)

# while True:

#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='faheem29905',cursor_factory=RealDictCursor) 
#         cursor = conn.cursor()
#         print("connection was a success!")
#         break 
#     except Exception as error:
#         print("error was ",error)
#         time.sleep(3)
