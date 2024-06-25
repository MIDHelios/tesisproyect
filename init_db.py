from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class DB:
    def __init__(self):
        self.engine = create_engine('sqlite:///site.db')
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

db = DB()
