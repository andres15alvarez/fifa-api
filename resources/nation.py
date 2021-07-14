from flask_restful import Resource
from utils.http_status import HttpStatus
from models.nation import Nation, NationSchema

nation_schema = NationSchema()

class NationResource(Resource):

    def get(self, id):
        nation = Nation.query.get_or_404(id)
        dumped_nation = nation_schema.dump(nation)
        return dumped_nation, HttpStatus.ok_200.value