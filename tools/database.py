from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, registry

from Config import Config

DATABASE_URL= Config

engine = create_engine(Config.DATABASE_URL, echo=False, future=True)

mapper_registry = registry()
metadata = mapper_registry.metadata

Base = declarative_base()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine, future=True)
