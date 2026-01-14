import json
def config_loader():
    with open("config.json","r") as file:
     return json.load(file)