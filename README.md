# fifa-api
### An API developed in Python :snake: with Flask, Flask-restful, SQLAlchmey, Marshmallow and PostgreSQL :elephant:
This API was developed consuming the API of FIFA 21. Only for educational purposes.

## Resources
### Player
| URL                    | Method | Description                                                                              |
| :----------------------|:------:|:-----------------------------------------------------------------------------------------|
| /api/player            | GET    | Return a list of 20 players (paginated) with their respective club, nation and positions |
| /api/player/<int:id>   | GET    | Return the information of the player, his club, nation and positions                     |

### Club
| URL                    | Method | Description                                                                            |
| :----------------------|:------:|:---------------------------------------------------------------------------------------|
| /api/club              | GET    | Return a list of 20 clubs (paginated) with their respective players                    |
| /api/club/<int:id>     | GET    | Return the information of the club, with their respective players                      |

### Nation
| URL                    | Method | Description                                                                            |
| :----------------------|:------:|:---------------------------------------------------------------------------------------|
| /api/nation            | GET    | Return a list of 20 nations (paginated) with their respective players                  |
| /api/nation/<int:id>   | GET    | Return the information of the nation, with their respective players                    |
