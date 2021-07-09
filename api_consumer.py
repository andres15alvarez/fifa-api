import psycopg2
import requests
import json
from collections import namedtuple
from private import USERNAME, PASSWORD, DATABASE
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

URL = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page="
response = requests.get(URL + "1")
json_data = json.loads(response.text)
TOTAL_PAGES = json_data['totalPages']

items_tuple = []
Item = namedtuple('Item', ['name', 'birthdate', 'club', 'nation', 'position'])
for i in range(1, TOTAL_PAGES+1):
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

conn = psycopg2.connect(
    database=DATABASE,
    password=PASSWORD,
    user=USERNAME
)
cur = conn.cursor()

conn.commit()
cur.close()
conn.close()