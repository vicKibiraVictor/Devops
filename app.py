








from sqlalchemy import create_engine


postgres_uri = "postgresql://root:root@localhost:5432/my_database"

engine = create_engine(postres_uri)

engine.connect()