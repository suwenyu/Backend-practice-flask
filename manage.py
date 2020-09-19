from api import create_app
from api import db
from api import socketio
from api.main import blueprint
from api.model import user
from api.schema import schema
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_script import Shell
import os
import unittest

app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
app.register_blueprint(blueprint)
app.app_context().push()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

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


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == "__main__":
    manager.run()
