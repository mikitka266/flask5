import databases as database
import sqlalchemy
from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.Metadata()
engine  = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

