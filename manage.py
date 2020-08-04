from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from project.models import User
import datetime

from project import app, db

app.config.from_object('config.DevelopmentConfig')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(
        username="admin2",
        name="admin",
        surname="admin",
        email="admin@example.com",
        password="admin",
        admin=True,
        verified=True)
    )
    db.session.commit()


if __name__ == '__main__':
    manager.run()

# previous code
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager
#
# app = Flask(__name__)
# app.config.from_object('config.DevelopmentConfig')
#
# db = SQLAlchemy(app)
#
# migrate = Migrate(app, db)
# manager = Manager(app)
#
# manager.add_command('db', MigrateCommand)
#
# # INSERT MODELS HERE
# from project.models import *
#
# if __name__ == '__main__':
#     manager.run()
