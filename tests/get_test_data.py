import json
from data_structures.datacenter import Datacenter


def get_data():
    with open('response.json') as json_file:
        data = json.load(json_file)
        return [
            Datacenter(key, value)
            for key, value in data.items()
        ]
