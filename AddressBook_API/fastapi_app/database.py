from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:example@0.0.0.0:5432/db_AddressBook"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:example@db/db_AddressBook"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'options': '-csearch_path={}'.format('xaldigital')}
)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()