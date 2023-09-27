import databases as database
import sqlalchemy
from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.Metadata()

users = sqlalchemy.Table(
"users",
metadata,
sqlalchemy.Column("id", sqlalchemy.Integer,
primary_key=True),
sqlalchemy.Column("firstname", sqlalchemy.String(32)),
sqlalchemy.Column("lastname", sqlalchemy.String(32)),
sqlalchemy.Column("email", sqlalchemy.String(128)),
sqlalchemy.Column("password", sqlalchemy.String(128))
)

engine  = sqlalchemy.create_engine(DATABASE_URL,
                                  connect_args={'check same thread': False})

metadata.create_all(engine)

