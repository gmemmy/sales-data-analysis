from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import datetime
import os

Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.date.today)
    region = Column(String(50))
    amount = Column(Float)

load_dotenv()

# get database credentials from environment variables
user = os.getenv("DB_USER", "user")
password = os.getenv("MYSQL_PASSWORD", "userpassword")
host = os.getenv("MYSQL_HOST", "localhost")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DATABASE", "sales")

connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# we check for any existing sales data
# if not, populate with sample data
if session.query(Sale).count() == 0:
    sample_sales= [
      Sale(date=datetime.date(2023, 1, 1), region='North', amount=1000),
      Sale(date=datetime.date(2023, 1, 2), region='South', amount=1500),
      Sale(date=datetime.date(2023, 1, 3), region='East', amount=2000),
      Sale(date=datetime.date(2023, 1, 4), region='West', amount=2500)
    ]
    session.add_all(sample_sales)
    session.commit()
    