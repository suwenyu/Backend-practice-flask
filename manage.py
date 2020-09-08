import os
import unittest

from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_script import Shell

from api import create_app
from api import db
from api import socketio
from api.main import blueprint
from api.model import user

app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, user=user)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def run():
    socketio.run(app)


@manager.command
def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()
