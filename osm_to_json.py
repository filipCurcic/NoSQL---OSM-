import json
import xmltodict

def osm_to_json(input_path, output_path):
    part = ""
    counter = 0
    file_counter = 0
    with open(input_path+".osm", mode="r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            part += line
            counter += 1
            if counter > 10000 and line.startswith("</"):
                file_counter += 1
                print(file_counter)
                with open(output_path+str(file_counter)+".json", mode="w", encoding="utf-8") as file:
                    file.write(json.dumps(xmltodict.parse(part+"\n</osm>")))
                part = "<osm>\n"
                counter = 0
    return file_counter
