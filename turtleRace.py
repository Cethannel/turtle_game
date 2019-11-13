from random import randint
from turtle import *
import os
import json

penup()

goto(-140, 140)
speed(10000)

for step in range(15):
    write(step, align = 'center')
    right(90)
    forward(10)
    pendown()
    for dash in range(7):
        forward(10)
        penup()
        forward(10)
        pendown()
    forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

sam = Turtle()
sam.color('green')
sam.shape('turtle')

sam.penup()
sam.goto(-160, 40)
sam.pendown()

ham = Turtle()
ham.color('yellow')
ham.shape('turtle')

ham.penup()
ham.goto(-160, 10)
ham.pendown()

for rotate in range(36):
    ada.right(10)
    bob.right(10)
    sam.right(10)
    ham.right(10)

for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    sam.forward(randint(1, 5))
    ham.forward(randint(1, 5))


#print(__path__)

'''
with open('*/scores.json') as json_file:
    data = json.load(json_file)
    turtles = {"ada": ada.xcor(), "bob": bob.xcor(), "sam": sam.xcor(), "ham": ham.xcor()}
    winner = max(turtles, key=turtles.get)
    data['turtles'][winner] = data['turtles'][winner] + 1
    json.dump(data, json_file)
'''

#print(os.getcwd(), 'test')

#input()

with open('scores.json', 'r+') as json_file:
    data = json.load(json_file)
    if ada.xcor() > bob.xcor():
        if ada.xcor() > sam.xcor():
            if ada.xcor() > ham.xcor():
                data['turtles']['ada'] = data['turtles']['ada'] + 1
            else:
                data['turtles']['ham'] = data['turtles']['ham'] + 1
        elif sam.xcor() > ham.xcor():
            data['turtles']['sam'] = data['turtles']['sam'] + 1
        else:
            data['turtles']['ham'] = data['turtles']['ham'] + 1
    elif bob.xcor() > sam.xcor():
        if bob.xcor() > ham.xcor():
            data['turtles']['bob'] = data['turtles']['bob'] + 1
        else:
            data['turtles']['ham'] = data['turtles']['ham'] + 1
    elif sam.xcor() > ham.xcor():
        data['turtles']['sam'] = data['turtles']['sam'] + 1
    else:
        data['turtles']['ham'] = data['turtles']['ham'] + 1
    json_file.seek(0)
    json.dump(data, json_file, indent=4)
    json_file.truncate()