import os
import msvcrt

while True:
    os.system('turtleRace.py')
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            break

print('test')