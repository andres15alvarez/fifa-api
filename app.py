from flask import Flask, Blueprint
from flask_restful import Api
from flask_migrate import Migrate
from models import orm
from resources import blueprint, api

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    orm.init_app(app)
    app.register_blueprint(blueprint, url_prefix='/api')
    migrate = Migrate(app, orm)
    return app

app = create_app('config')