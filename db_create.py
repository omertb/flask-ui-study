# from project import db
from project.models import *


# create the database and the db table
db.create_all()

# insert data
db.session.add(User("admin", "admin", "admin@example.com"))
db.session.add(User("user1", "user1", "user1@example.com"))
# User.query.filter_by(username='admin').delete()
# db.session.add(Network("Test-Wireless", "wireless"))
# db.session.add(Network("Test-Switch", "switch"))


# commit the changes
db.session.commit()