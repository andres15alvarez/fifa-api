from models import orm

PlayerPosition = orm.Table(
    'PlayerPosition',
    orm.Column('player_id', orm.Integer, orm.ForeignKey('Player.id')),
    orm.Column('position_id', orm.Integer, orm.ForeignKey('Position.id'))
)