from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://dario208:123456@localhost/magasy', echo=True)
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()