#   wall module
# creating the ball and controlling its movement, bounces and acceleration

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_step = 5
        self.y_step = 5
        self.move_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bound_x(self):
        self.x_step *= -1
        self.move_speed *= 0.9

    def bound_y(self):
        self.y_step *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_step *= -1
        self.move_speed = 0.04
