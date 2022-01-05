#   paddel module
# creating the paddel and controlling its movement

from turtle import Turtle


class Paddel(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.color("white")
        self.goto(x, y)

    def right_move(self):
        if self.xcor() < 310:
            self.forward(40)

    def left_move(self):
        if self.xcor() > -310:
            self.backward(40)
