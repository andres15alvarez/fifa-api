from flask import Flask
from flask_migrate import Migrate
from flask_graphql import GraphQLView
from models import orm
from resources import blueprint, api
from resources.graphql.schema import schema

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    orm.init_app(app)
    app.register_blueprint(blueprint, url_prefix='/api')
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    migrate = Migrate(app, orm)
    return app

app = create_app('config')