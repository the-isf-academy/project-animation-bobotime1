from turtle import *

def apple(size):
    pensize(10)
    color("black")
    begin_fill()
    for i in range(10):
            if i == 0:
                forward(size/5)
                right(10)
                forward(size/5)
                right(5)
                forward(size/5)
                right(15)
            if i == 1:
                forward(size/10)
                right(15)
                forward(size/10)
                right(15)
                forward(size/10)
                right(30)
                forward(size/10)
                right(5)
            if i == 2:
                forward(size/(10/3))
                right(5)
                forward(size/(10/3))
                right(10)
                forward(size/(10/3))
                right(15)
            if i == 3:
                forward(size/10)
                right(45)
                forward(size/5)
                right(5)
            if i == 4:
                forward(size/5)
                right(5)
                forward(size/10)
                right(10)
                forward(size/10)
                right(10)
                forward(size/10)
                left(10)
                forward(size/10)
                right(5)
            if i == 5:
                forward(size/5)
                right(45)
                forward(size/10)
                right(15)
            if i == 6:
                forward(size/(10/3))
                right(10)
                forward(size/(10/3))
                right(5)
                forward(size/(10/3))
                right(5)
            if i == 7:
                forward(size/10)
                right(30)
                forward(size/10)
                right(15)
                forward(size/10)
                right(15)
                forward(size/10)
                right(15)
            if i == 8:
                forward(size/5)
                right(11)
                forward(size/(50/9))
                left(85)
                forward(size/15)
                color("red")
                end_fill()
                color("brown")

            if i == 9:
                forward(size/(5/2))
                right(70)
                forward(size/10)
                color("red")
                end_fill()

def knife(size):
    pensize(5)
    color("black")
    begin_fill()






input()
