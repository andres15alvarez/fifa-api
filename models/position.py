from models import orm, ma, ResourceAddUpdateDelete, fields, validate
from .player_position import PlayerPosition

class Position(orm.Model, ResourceAddUpdateDelete):

    __tablename__ = 'Position'
    id = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String(3), unique=True, nullable=False)
    player = orm.relationship('Player', secondary=PlayerPosition, backref=orm.backref('position', lazy='dynamic', order_by='Position.name'))

    def __init__(self, name):
        self.name = name

    @classmethod
    def is_name_unique(cls, id, name):
        position_name = cls.query.filter_by(name=name).first()
        if position_name is None:
            return False
        else:
            return position_name.id == id


class PositionSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=3))
    url = ma.URLFor('api.positionresource', id='<id>', _external=True)
    players = fields.Nested('PlayerSchema', many=True, only=('name', ))