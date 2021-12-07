from turtle import *
import settings
import time
from object import apple, knife, knife_in_apple
from helpers import fly, no_delay, restore_state_when_finished
from misc import sky_background, ts_color, words, ts_background, k_positioning, a_positioning, ts_words

def draw_animation(num_frames, sleeptime):
    sky_background()
    j = -300
    k = 400
    v = 220
    m = 0
    hideturtle()
    fly(0, -300)
    "Intializes values for functions used later as well as change the background color to skyblue."
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
                "Moves the apple upwards while rotating the turtle so the apple drawn will also rotate."
                "After drawing the apple, the drawing gets cleared for the next frame, but using the j value the turtle will change and make the apple move upwards."

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
                "By changing the j value's change and the rotating each frame an illusion could be created for the apple slowing down due to gravity."

            elif i in range(111, 121):
                apple(100)
                j = j - 2
                fly(0, j)
                screen.update()
                time.sleep(sleeptime)
                clear()
                "The apple no longer rotates and also starts moving downwards"

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
                "Changes the background color to orange, print words, as well as draw an apple in the last location it was drawn. There isn't a clear function so the drawing remains the same without change."
                "This creates an illusion that the animation has paused/stopped, but in reality the turtle is simply drawing objects over and over in the same location."

            elif i in range(201, 202):
                screen.update()
                time.sleep(sleeptime)
                clear()
                "Clears the previous words and apple, which sets up to draw the function ts_background in the next frame."

            elif i in range(202, 203):
                ts_background()
                right(38)
                "Draws the background with color and apple but without the words. The turtle is also repositioned to face the correct angle for the knife."

            elif i in range(203, 213):
                k_positioning(k)
                knife(50)
                k = k - 10
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()
                "Draws the knife moving towards the apple but with the apple still remaining in the same original spot. a_positioning is used to constantly re-direct the turtle to face the correct direction"

            elif i in range(213, 223):
                k_positioning(k)
                knife(50)
                k = k - 1
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()
                "Draws the knife moving towards the apple but at a slower speed each frame. This creates an illusion that the knife is slowing down."

            elif i in range(223, 273):
                k_positioning(k)
                knife(50)
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()
                "Draws the knife and the apple at a standstill position where both object don't move."

            elif i in range(273, 274):
                sky_background()
                clear()
                "Clears the orange screen color and replaces it with skyblue."

            elif i in range(274, 279):
                sky_background()
                words()
                k_positioning(k)
                knife(50)
                k = k - 7
                a_positioning()
                screen.update()
                time.sleep(sleeptime)
                clear()
                "Moves the knife towards the apple while printing words and keeping a blue background."

            elif i in range(279, 299):
                knife_in_apple(v, m, 100)
                v = v - 30
                m = m - 30
                screen.update()
                time.sleep(sleeptime)
                clear()
                "Replaces the apple and knife objects with the knife_in_apple object which flies off screen at a high speed. Creates the illusion that the apple was impaled and is now flying off screen due to the force from the strike."

            else:
                setheading(0)
                "Resets the turtle's direction to face right for the animation to loop."

def main():
    for i in range(settings.NUMREPEATS):
        draw_animation(settings.NUMFRAMES, settings.SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()
