import click
from app.database import SessionLocal
from app.models import Product


@click.group()
def cli():
    """Products CRUD CLI"""
    pass


@cli.command()
def list():
    """List all products"""
    session = SessionLocal()
    try:
        products = session.query(Product).all()

        if not products:
            click.echo("No products found.")
            return

        for product in products:
            click.echo(f"ID: {product.id} | Name: {product.name} | Price: {product.price}")
    finally:
        session.close()


@cli.command()
@click.argument("name")
@click.argument("price", type=float)
def add(name, price):
    """Add product"""
    session = SessionLocal()
    try:
        product = Product(name=name, price=price)
        session.add(product)
        session.commit()
        click.echo("Product added.")
    finally:
        session.close()


@cli.command()
@click.argument("product_id", type=int)
def get(product_id):
    """Get product"""
    session = SessionLocal()
    try:
        product = session.query(Product).filter(Product.id == product_id).first()

        if not product:
            click.echo("Product not found.")
            return

        click.echo(f"{product.id} - {product.name} - {product.price}")
    finally:
        session.close()


@cli.command()
@click.argument("product_id", type=int)
@click.argument("name")
@click.argument("price", type=float)
def update(product_id, name, price):
    """Update product"""
    session = SessionLocal()
    try:
        product = session.query(Product).filter(Product.id == product_id).first()

        if not product:
            click.echo("Product not found.")
            return

        product.name = name
        product.price = price
        session.commit()

        click.echo("Product updated.")
    finally:
        session.close()


@cli.command()
@click.argument("product_id", type=int)
def delete(product_id):
    """Delete product"""
    session = SessionLocal()
    try:
        product = session.query(Product).filter(Product.id == product_id).first()

        if not product:
            click.echo("Product not found.")
            return

        session.delete(product)
        session.commit()

        click.echo("Product deleted.")
    finally:
        session.close()