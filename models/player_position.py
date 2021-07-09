from models import orm

PlayerPosition = orm.Table(
    'PlayerPosition',
    orm.Column('playerId', orm.Integer, orm.ForeignKey('Player.id')),
    orm.Column('positionId', orm.Integer, orm.ForeignKey('Position.id'))
)