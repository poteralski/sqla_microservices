import click
from flask import Flask

from apps.flask_sqlalchemy.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_sqlalchemy.db'
db.init_app(app)
app.app_context().push()

@click.group()
def cli():
    "cli"


@click.command("rebuild")
def rebuild():
    db.create_all()
    """rebuild db and init data"""

@click.command("read")
def read():
    """read some data from db"""


@click.command("update")
def update():
    """update some data to db"""


cli.add_command(rebuild)
cli.add_command(read)
cli.add_command(update)
cli()
