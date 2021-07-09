from models import orm, ma, ResourceAddUpdateDelete, fields, validate
from .player_position import PlayerPosition

class Player(orm.Model, ResourceAddUpdateDelete):

    __tablename__ = 'Player'
    id = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String(100), unique=True, nullable=False)
    birthday = orm.Column(orm.DateTime)
    position = orm.relationship('Position', secondary=PlayerPosition, backref=orm.backref('player', lazy='dynamic', order_by='Player.name'))

    def __init__(self, name):
        self.name = name

    @classmethod
    def is_name_unique(cls, id, name):
        player_name = cls.query.filter_by(name=name).first()
        if player_name is None:
            return False
        else:
            return player_name.id == id


class PlayerSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=3, max=100))
    birthday = fields.Date()
    url = ma.URLFor('api.playerresource', id='<id>', _external=True)
    position = fields.Nested('PositionSchema', many=True, only=('name', ))