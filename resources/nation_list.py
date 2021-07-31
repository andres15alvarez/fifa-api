from flask import request, current_app
from flask_restful import Resource
from utils.http_status import HttpStatus
from utils.pagination_helper import PaginationHelper
from models.nation import Nation, NationSchema


nation_schema = NationSchema()


class NationListResource(Resource):

    def get(self):
        page_argument_name = current_app.config['PAGINATION_PAGE_ARGUMENT_NAME']
        page_number = request.args.get(page_argument_name, 1, type=int)
        name_searched = request.args.get('name', '', type=str)
        if name_searched:
            pagination_helper = PaginationHelper(
                page_number=page_number,
                query=Nation.query.filter(Nation.name.ilike(f'%{name_searched}%')),
                resource_for_url='api.nationlistresource',
                key_name='results',
                schema=nation_schema
            )
            result = pagination_helper.paginate_query()
            return result, HttpStatus.ok_200.value

        pagination_helper = PaginationHelper(
            page_number=page_number,
            query=Nation.query,
            resource_for_url='api.nationlistresource',
            key_name='results',
            schema=nation_schema
        )
        result = pagination_helper.paginate_query()
        return result, HttpStatus.ok_200.value
