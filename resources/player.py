from flask import request, jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from utils.http_status import HttpStatus
from utils.pagination_helper import PaginationHelper
from models import orm
from models.player import Player, PlayerSchema

player_schema = PlayerSchema()

class PlayerResource(Resource):

    def get(self, id):
        player = Player.query.get_or_404(id)
        dumped_player = player_schema.dump(player)
        return dumped_player, HttpStatus.ok_200.value