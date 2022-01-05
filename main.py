#   main module

from turtle import Screen
import time
from paddel import Paddel
from ball import Ball
from wall import Wall
from score import Scoreboard

hi_score_ = 0
score_ = 0

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Alex breakout game')
screen.tracer(0)

paddel = Paddel(x=0, y=-250)
score = Scoreboard(x=150, y=240, title='Score: ')
hi_score = Scoreboard(x=-220, y=240, title='Hi score: ')
game_over = Scoreboard(x=0, y=0, title=' ')
ball = Ball()

screen.listen()
screen.onkey(paddel.left_move, "Left")
screen.onkey(paddel.right_move, "Right")


def main_game():
    game_over.clear()
    game_is_on = True
    global score_
    global hi_score_
    wall = Wall()
    score.write_score(score_)
    hi_score.hi_score(hi_score_)

    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        bound = False
        # the cycle of checking the impact of the ball with a brick wall, keeping score
        for brick in wall.wall_bricks:
            brick_y = brick.ycor() - 21
            if ball.ycor() > brick_y and ball.distance(brick) < 42 and not bound:
                wall.wall_bricks.remove(brick)
                brick.ht()
                bound = True
                score_ += 1
                score.write_score(score_)
                ball.bound_y()

        if ball.xcor() > 380:
            ball.bound_x()

        if ball.xcor() < -380:
            ball.bound_x()

        if ball.ycor() > 280:
            ball.bound_y()

        if ball.ycor() < -225 and ball.distance(paddel) < 80:
            ball.bound_y()

        # processing the end of the game when the ball has passed the paddle
        if ball.ycor() < -240:
            ball.reset_position()
            if hi_score_ < score_:
                hi_score_ = score_
                hi_score.hi_score(hi_score_)
            score_ = 0
            score.write_score(score_)
            game_is_on = False
            for brick in wall.wall_bricks:
                brick.ht()
            wall.wall_bricks.clear()
            ball.clear()
            game_over.game_over()


main_game()

screen.onkey(main_game, "space")

screen.exitonclick()
