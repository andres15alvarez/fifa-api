from marshmallow import Schema, validate, fields, pre_load
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils.resource_aud import ResourceAddUpdateDelete

orm = SQLAlchemy()
ma = Marshmallow()

from .nation import Nation
from .club import Club
from .player import Player
from .position import Position
from .player_position import PlayerPosition