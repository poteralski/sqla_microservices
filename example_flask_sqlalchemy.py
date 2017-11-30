import click
import time
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from apps.flask_sqlalchemy.models import db, Example

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_sqlalchemy.db'
app.config['SQLALCHEMY_ECHO'] = True
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
    time.sleep(5)
    while True:
        print("reading")
        example = db.session.query(Example).get(1)
        # print(example.value)
        # db.session.expire_all()
        print(example.value)
        time.sleep(1)


@click.command("update")
def update():
    """update some data to db"""
    while True:
        print("updating")
        example = db.session.query(Example).get(1)
        example.value += 1
        db.session.close()
        db.session.add(example)
        db.session.commit()
        db.session.remove()
        time.sleep(1)

@click.command("admin")
def admin():
    """run admin"""
    a = Admin()
    a.init_app(app)
    a.add_view(ModelView(Example, db.session))

    @app.teardown_request
    def remove_session(exception=None):
        db.session.remove()

    app.run()


cli.add_command(rebuild)
cli.add_command(read)
cli.add_command(update)
cli.add_command(admin)
cli()
