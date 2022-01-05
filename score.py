#   score    module
# creating and maintaining a scoreboard, displaying "GAME OVER" at the end of the game

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x, y, title):
        super().__init__()
        self.goto(x, y)
        self.color("white")
        self.hideturtle()
        self.title = title
        self.init_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER! press 'Space' for another game", move=False, align="center", font=("Arial", 16, "normal"))

    def init_scoreboard(self):
        self.clear()
        self.write(f"{self.title} 0", move=False, align="center", font=("Arial", 28, "normal"))

    def write_score(self, score_):
        self.clear()
        self.write(f"Score:  {score_}", move=False, align="center", font=("Arial", 28, "normal"))

    def hi_score(self, hi_score_):
        self.clear()
        self.write(f"Hi score:  {hi_score_}", move=False, align="center", font=("Arial", 28, "normal"))
