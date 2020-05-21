import os
from osm_to_json import osm_to_json

def load_osm_data():
    files_number = 0
    # input_path = os.path.dirname(__file__) + "/../azores-latest"
    input_path =  "C://Users/Filip/Documents/Faks/NoSQL Baze/NoSQL - 2. Kolokvijum/andorra-latest"
    # output_folder = os.path.dirname(__file__) + "/../azores-latest-json"
    output_folder = "C://Users/Filip/Documents/Faks/NoSQL Baze/NoSQL - 2. Kolokvijum/files_andorra"
    output_file_name = "andorra"
    output_path = output_folder+"/"+output_file_name
    if os.path.exists(output_folder):
        path, dirs, files = next(os.walk(output_folder))
        files_number = len(files)
    if not os.path.exists(output_path+"1.json"):
        files_number = osm_to_json(input_path, output_path)
    return files_number, output_path