from turtle import *

def apple(size):

    for i in range(9):
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
                forward(size/5)
                right(10)
                forward(5)
                left(10)
                forward(5)
                right(5)
            if i == 5:
                forward(10)
                right(45)
                forward(5)
                right(15)
            if i == 6:
                forward(15)
                right(10)
                forward(15)
                right(5)
                forward(15)
                right(5)
            if i == 7:
                forward(5)
                right(30)
                forward(5)
                right(15)
                forward(5)
                right(15)
                forward(5)
                right(15)
            if i == 8:
                forward(10)
                right(11)
                forward(9)
                left(85)
                forward(20)



apple(50)




input()
