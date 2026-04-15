from app.database import Base, engine
from app.models import Product
from app.cli import cli

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    cli()