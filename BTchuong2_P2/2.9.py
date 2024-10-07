import json

data = {
    'name': 'NgTheAnh',
    'age': 19,
    'location': 'Bac Ninh'
}

json_data = json.dumps(data, sort_keys=True, indent=4)
print(json_data)
