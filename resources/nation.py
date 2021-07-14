from flask import request, jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from utils.http_status import HttpStatus
from utils.pagination_helper import PaginationHelper
from models import orm
from models.nation import Nation, NationSchema

nation_schema = NationSchema()

class NationResource(Resource):

    def get(self, id):
        nation = Nation.query.get_or_404(id)
        dumped_nation = nation_schema.dump(nation)
        return dumped_nation, HttpStatus.ok_200.value