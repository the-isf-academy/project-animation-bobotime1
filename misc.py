from turtle import *
from helpers import fly
from object import knife, apple

def sky_background():
    a = Screen()
    a.bgcolor("skyblue")

def ts_color():
    b = Screen()
    b.bgcolor("darkorange")

def ts_words():
    fly(215, -100)
    write("Watch - Luna Dial", font = ("Verdana", 15, "normal"))

def words():
    fly(150, -100)
    write("Time has begun to move again", font = ("Verdana", 15, "normal"))

def k_positioning(x_cord):
    fly(x_cord, 108)

def a_positioning():
    fly(0, 108)
    setheading(130)
    apple(100)
    setheading(92)


def ts_background():
    ts_color()
    fly(0, 108)
    apple(100)
