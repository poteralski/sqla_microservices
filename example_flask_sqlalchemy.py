import click
import time
from flask import Flask

from apps.flask_sqlalchemy.models import db, Example

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_sqlalchemy.db'
db.init_app(app)
app.app_context().push()

@click.group()
def cli():
    "cli"


@click.command("rebuild")
def rebuild():
    db.drop_all()
    db.create_all()
    example = Example(value=1)
    db.session.add(example)
    db.session.commit()
    """rebuild db and init data"""

@click.command("read")
def read():
    """read some data from db"""
    while True:
        print("reading")
        example = db.session.query(Example).get(1)
        print(example.value)
        time.sleep(1)


@click.command("update")
def update():
    """update some data to db"""
    while True:
        print("updating")
        example = db.session.query(Example).get(1)
        example.value += 1
        db.session.add(example)
        db.session.commit()
        time.sleep(1)

cli.add_command(rebuild)
cli.add_command(read)
cli.add_command(update)
cli()
