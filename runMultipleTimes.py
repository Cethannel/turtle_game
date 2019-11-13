import os

numTimes = 0

numTimes = int(input('Enter the number of times you would like the race to run:'))

for step in range(numTimes):
    os.system('turtleRace.py')