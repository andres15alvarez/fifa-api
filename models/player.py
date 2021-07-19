from models import orm, ma, ResourceAddUpdateDelete, fields, validate
from models.player_position import PlayerPosition

class Player(orm.Model, ResourceAddUpdateDelete):

    __tablename__ = 'Player'
    id = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String(100), nullable=False)
    birthdate = orm.Column(orm.DateTime)
    club_id = orm.Column(orm.Integer, orm.ForeignKey('Club.id', ondelete='CASCADE'), nullable=False)
    club = orm.relationship('Club', backref=orm.backref('players', lazy='dynamic', order_by='Player.name'))
    nation_id = orm.Column(orm.Integer, orm.ForeignKey('Nation.id', ondelete='CASCADE'), nullable=False)
    nation = orm.relationship('Nation', backref=orm.backref('players', lazy='dynamic', order_by='Player.name'))
    position = orm.relationship('Position', secondary=PlayerPosition, backref=orm.backref('Player', lazy='dynamic', order_by='Player.name'))

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
    birthdate = fields.Date()
    url = ma.URLFor('api.playerresource', id='<id>', _external=True)
    club = fields.Nested('ClubSchema', many=False, only=('id', 'name', 'url'))
    nation = fields.Nested('NationSchema', many=False, only=('id', 'name', 'url'))
    position = fields.Nested('PositionSchema', many=True, only=('name', ))