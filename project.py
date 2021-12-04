from turtle import *
import settings
import time
from object import apple, knife
from helpers import fly, no_delay, restore_state_when_finished
from misc import sky_background, ts_color, words, ts_background, k_positioning, a_positioning, ts_words

def draw_animation(num_frames, sleeptime):
    sky_background()
    j = -300
    k = 400
    speed(100)
    hideturtle()
    fly(0, -300)
    with no_delay():
        for i in range(num_frames):
            if i <= 40:
                left(10)
                apple(100)
                sky_background()
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

            elif i in range(141, 201):
                ts_color()
                ts_words()
                fly(0, j)
                apple(100)

            elif i in range(201, 202):
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(202, 203):
                ts_background()
                right(38)

            elif i in range(203, 213):
                k_positioning(k)
                knife(50)
                k = k - 8
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(213, 223):
                k_positioning(k)
                knife(50)
                k = k - 2
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(213, 223):
                k_positioning(k)
                knife(50)
                k = k - 2
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(223, 273):
                k_positioning(k)
                knife(50)
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()

            elif i in range(273, 283):
                sky_background()
                words()
                k_positioning(k)
                knife(50)
                k = k - 5
                a_positioning()

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
