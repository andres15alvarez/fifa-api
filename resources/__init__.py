from flask import Blueprint
from flask_restful import Api
from resources.player import PlayerResource
from resources.player_list import PlayerListResource

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

# TODO: Add resources
api.add_resource(PlayerListResource, '/player')
api.add_resource(PlayerResource, '/player/<int:id>')