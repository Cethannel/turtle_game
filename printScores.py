import json

with open('scores.json') as json_file:
    data = json.load(json_file)
    print('Red scored:' ,data['turtles']['ada'])
    print('Blue scored:' ,data['turtles']['bob'])
    print('Green scored:' ,data['turtles']['sam'])
    print('Yellow scored:' ,data['turtles']['ham'])

input()