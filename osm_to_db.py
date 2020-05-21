import copy
import json
import pymongo
from load_osm_data import load_osm_data

files_number, output_path = load_osm_data()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["nosql2kolokvijum"]
andorra = mydb["andorra"]

top_left_coordinates = {"lat":42.5112, "lon": 1.5236}
bottom_left_coordinates = {"lat": 42.5045, "lon": 1.5236}

top_right_coordinates = {"lat":42.5112, "lon": 1.5369} 
botom_right_coordinates = {"lat":42.5045, "lon": 1.5369}



for i in range(files_number):
    with open(output_path+str(i+1)+".json", mode="r", encoding="utf-8") as file:
        print(i+1)
        data = json.load(file)
        try:
            data['osm']['node'] = list(filter(lambda x: float(x['@lat']) < 42.5112, data['osm']['node'] ))
            data['osm']['node'] = list(filter(lambda x: float(x['@lat']) > 42.5045, data['osm']['node'] ))
            data['osm']['node'] = list(filter(lambda x: float(x['@lon']) < 1.5369, data['osm']['node'] ))
            data['osm']['node'] = list(filter(lambda x: float(x['@lon']) > 1.5236, data['osm']['node'] ))
            andorra.insert_one(data)
            
        except (pymongo.errors.DocumentTooLarge, KeyError) as e:
            data_1 = copy.deepcopy(data)
            data_2 = copy.deepcopy(data)
            try:
                data_1["osm"]["node"] = data_1["osm"]["node"][len(
                    data_1["osm"]["node"])//2:]
                data_2["osm"]["node"] = data_2["osm"]["node"][:len(
                    data_2["osm"]["node"])//2]
                data_1["osm"]["way"] = data_1["osm"]["way"][len(
                    data_1["osm"]["way"])//2:]
                data_2["osm"]["way"] = data_2["osm"]["way"][:len(
                    data_2["osm"]["way"])//2]
                data_1["osm"]["relation"] = data_1["osm"]["relation"][len(
                    data_1["osm"]["relation"])//2:]
                data_2["osm"]["relation"] = data_2["osm"]["relation"][:len(
                    data_2["osm"]["relation"])//2]
            except KeyError:
                pass
            andorra.insert_one(data_1)
            if '_id' in data_2:
                del data_2['_id']
            andorra.insert_one(data_2)
