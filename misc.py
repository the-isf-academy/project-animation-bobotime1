from turtle import *
from helpers import fly
from object import knife, apple

def sky_background():
    a = Screen()
    a.bgcolor("skyblue")
#Fills the screen with the color skyblue, creating a background for my animation

def ts_color():
    b = Screen()
    b.bgcolor("darkorange")
#Fills the screen with the color drakorange.

def ts_words():
    fly(215, -100)
    write("Watch - Luna Dial", font = ("Verdana", 15, "normal"))
#Prints out words after flying to the side of the screen.

def words():
    fly(150, -100)
    write("Time has begun to move again", font = ("Verdana", 15, "normal"))
#Prints out words after flying to the side of the screen.

def k_positioning(x_cord):
    fly(x_cord, 108)
#Repositions turtle to a coordinate that changes to draw the knife

def a_positioning():
    fly(0, 108)
    setheading(130)
    apple(100)
    setheading(92)
#Repositions turtle to a set coordinate before drawing the apple in the middle of the screen

def ts_background():
    ts_color()
    fly(0, 108)
    apple(100)
#Draws a background with an apple and the darkorange color
