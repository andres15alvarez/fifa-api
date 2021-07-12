import psycopg2
import requests
import json
from tqdm import tqdm
from collections import namedtuple
from private import USERNAME, PASSWORD, DATABASE
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

URL = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page="
response = requests.get(URL + "1")
json_data = json.loads(response.text)
TOTAL_PAGES = json_data['totalPages']

Item = namedtuple('Item', ['name', 'birthdate', 'club', 'nation', 'position'])
Player = namedtuple('Player', ['name', 'birthdate'])
PlayerPositions = namedtuple('PlayerPosition', ['name', 'position'])

items_tuple = []
for i in tqdm(range(1, TOTAL_PAGES+1), desc='Consuming the api'):
    response = requests.get(URL + f'{i}')
    json_data = json.loads(response.text)
    items = json_data['items']

    for item in items:
        item_tuple = Item(
            name=item['commonName'] if item['commonName']!='' \
                 else ''.join((item["firstName"], " ", item["lastName"])),
            birthdate=item['birthdate'],
            club=item["club"]["name"],
            nation=item["nation"]["abbrName"],
            position=item["position"]
        )
        items_tuple.append(item_tuple)

items = list(set(items_tuple))
unique_clubs = list(set([item.club for item in items]))
unique_nations = list(set([item.nation for item in items]))
unique_positions = list(set([item.position for item in items]))
unique_players = list(set([Player(name=item.name, 
                                  birthdate=item.birthdate) for item in items]))
nation_by_player = dict([(item.name, item.nation) for item in items])
club_by_player = dict([(item.name, item.club) for item in items])
positions_by_player = list(set([PlayerPositions(name=item.name,
                                                position=item.position) for item in items]))

conn = psycopg2.connect(
    database=DATABASE,
    password=PASSWORD,
    user=USERNAME
)
cur = conn.cursor()

for nation in tqdm(unique_nations , desc='Inserting nations'):
    cur.execute('INSERT INTO "Nation" (name) VALUES (%s);', (nation, ))

for club in tqdm(unique_clubs, desc='Inserting clubs'):
    cur.execute('INSERT INTO "Club" (name) VALUES(%s);', (club, ))

for position in tqdm(unique_positions, desc='Inserting positions'):
    cur.execute('INSERT INTO "Position" (name) VALUES(%s);', (position, ))

cur.execute('SELECT name, id FROM "Club";')
clubs = dict(cur.fetchall())

cur.execute('SELECT name, id FROM "Nation";')
nations = dict(cur.fetchall())

cur.execute('SELECT name, id FROM "Position";')
positions = dict(cur.fetchall())


for player in tqdm(unique_players, desc='Inserting players'):
    cur.execute('INSERT INTO "Player" (name, birthdate, club_id, nation_id) VALUES (%s, %s, %s, %s);',
                (player.name, player.birthdate, clubs[club_by_player[player.name]], nations[nation_by_player[player.name]]))

cur.execute('SELECT name, id FROM "Player";')
players = dict(cur.fetchall())

for player in tqdm(positions_by_player, desc='Inserting playerpositions'):
    cur.execute('INSERT INTO "PlayerPosition" (player_id, position_id) VALUES (%s, %s);',
               (players[player.name], positions[player.position]))

conn.commit()
cur.close()
conn.close()
print('Api consumer executed successfully')