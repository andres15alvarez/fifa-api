from models import orm, ma, ResourceAddUpdateDelete, fields, validate

class Club(orm.Model, ResourceAddUpdateDelete):

    __tablename__ = 'Club'
    id = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String(100), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    @classmethod
    def is_name_unique(cls, id, name):
        nation_name = cls.query.filter_by(name=name).first()
        if nation_name is None:
            return False
        else:
            return nation_name.id == id


class ClubSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=3, max=100))
    players = fields.Nested('PlayerSchema', many=True, exclude=('club', ))
    url = ma.URLFor('api.clubresource', id='<id>', _external=True)