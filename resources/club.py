from flask import request, jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from utils.http_status import HttpStatus
from utils.pagination_helper import PaginationHelper
from models import orm
from models.club import Club, ClubSchema

club_schema = ClubSchema()

class ClubResource(Resource):

    def get(self, id):
        club = Club.query.get_or_404(id)
        dumped_club = club_schema.dump(club)
        return dumped_club, HttpStatus.ok_200.value