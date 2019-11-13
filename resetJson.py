import json

with open('scores.json', 'r+') as json_file:
    data = json.load(json_file)
    data['turtles']['ada'] = 0
    data['turtles']['bob'] = 0
    data['turtles']['sam'] = 0
    data['turtles']['ham'] = 0
    json_file.seek(0)
    json.dump(data, json_file, indent=4)
    json_file.truncate()