from turtle import *
import settings
import time
from object import apple, knife
from helpers import fly, no_delay, restore_state_when_finished

def draw_animation(num_frames, sleeptime):
    j = -300
    speed(100)
    fly(0, -300)
    hideturtle()
    with no_delay():
        for i in range(num_frames):
            if i <= 40:
                left(10)
                apple(100)
                j = j + 8
                fly(0, j)
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(41, 71):
                left(8)
                apple(100)
                j = j + 5
                fly(0, j)
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(71, 111):
                left(5)
                apple(100)
                j = j + 2
                fly(0, j)
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(111, 121):
                apple(100)
                j = j - 2
                fly(0, j)
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(121, 131):
                apple(100)
                j = j - 5
                fly(0, j)
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(131, 141):
                apple(100)
                j = j - 8
                fly(0, j)
                screen.update()
                time.sleep(sleeptime)
                clear()




def main():
    for i in range(settings.NUMREPEATS):
        draw_animation(settings.NUMFRAMES, settings.SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()
