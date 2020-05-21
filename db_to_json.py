import copy
import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["nosql2kolokvijum"]
andorra = mydb["andorra"]


andorra_data = [i for i in andorra.find({})]

nodes = []


for n in andorra_data:
    if 'node' in n['osm']:
        nodes.append(n['osm']['node'])


combined_nodes = []
for i in nodes:
    combined_nodes += i
tags = []
for m in combined_nodes:
    if 'tag' in m:
        tags.append(m['tag'])

streets = []

for t in tags:
    if type(t) is dict:
        pass
    if type(t) is list:
        for tag in t:
            if tag['@k'] == 'addr:street':
                streets.append(tag['@v']) if tag['@v'] not in streets else None

streets_json = {}
streets_json['streets'] = []
for s in streets:
    streets_json['streets'].append({'Street name': s})

with open('streets.json', 'w') as outfile:
    json.dump(streets_json, outfile)
