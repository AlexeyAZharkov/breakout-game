#   wall module
# creating a wall of "bricks"

from turtle import Turtle


class Wall:

    def __init__(self):
        self.wall_bricks = []
        self.create_wall()

    def create_wall(self):
        for y in range(100, 240, 20):
            for x in range(-360, 380, 80):
                new_brick = Turtle(shape='square')
                new_brick.shapesize(stretch_wid=1, stretch_len=4, outline=3)
                new_brick.color('white')
                new_brick.pencolor('black')
                new_brick.penup()
                new_brick.goto(x=x, y=y)
                self.wall_bricks.append(new_brick)
