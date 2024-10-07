import json

data = {
    'name': 'DoThuyDuong',
    'age': 19,
    'location': 'Bac Kan'
}

json_data = json.dumps(data, sort_keys=True, indent=4)
print(json_data)
