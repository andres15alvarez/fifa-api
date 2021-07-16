import graphene
from graphene import relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.player import Player as PlayerModel
from models.nation import Nation as NationModel
from models.club import Club as ClubModel
from models.position import Position as PositionModel

class Player(SQLAlchemyObjectType):

    class Meta:
        model = PlayerModel
        interfaces = (relay.Node, )


class Nation(SQLAlchemyObjectType):

    class Meta:
        model = NationModel
        interfaces = (relay.Node, )


class Club(SQLAlchemyObjectType):

    class Meta:
        model = ClubModel
        interfaces = (relay.Node, )


class Position(SQLAlchemyObjectType):
    
    class Meta:
        model = PositionModel
        interfaces = (relay.Node, )


class Query(ObjectType):

    node = relay.Node.Field()
    all_players = SQLAlchemyConnectionField(Player.connection)
    all_nations = SQLAlchemyConnectionField(Nation.connection)
    all_clubs = SQLAlchemyConnectionField(Club.connection)
    all_positions = SQLAlchemyConnectionField(Position.connection)

schema = graphene.Schema(query=Query)