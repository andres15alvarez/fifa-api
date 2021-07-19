from flask_restful import Resource
from utils.http_status import HttpStatus
from models.club import Club, ClubSchema

club_schema = ClubSchema()

class ClubResource(Resource):

    def get(self, id):
        club = Club.query.get_or_404(id)
        print(club)
        dumped_club = club_schema.dump(club)
        return dumped_club, HttpStatus.ok_200.value