import databases as database
import sqlalchemy
from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.Metadata()
engine  = sqlalchemy.create_engine(DATABASE_URL)

users = sqlalchemy.Table(
"users",
metadata,
sqlalchemy.Column("id", sqlalchemy.Integer,
primary_key=True),
sqlalchemy.Column("name", sqlalchemy.String(32)),
sqlalchemy.Column("email", sqlalchemy.String(128)),
)

metadata.create_all(engine)

