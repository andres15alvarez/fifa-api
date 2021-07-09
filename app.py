from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import orm
# from resources import service_blueprint

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    orm.init_app(app)
    blueprint = Blueprint('api', __name__)
    api = Api(blueprint)
    # TODO: Add resources
    app.register_blueprint(blueprint, url_prefix='/api')
    migrate = Migrate(app, orm)
    return app

app = create_app('config')