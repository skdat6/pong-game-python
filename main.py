from turtle import Screen, Turtle
from player import Player
from ball import *
from score import Scoreboard
import time

CIRCLE_RADIUS = 360
DEFAULT_LEFT = -350
DEFAULT_RIGHT = 350

scoreboard = Scoreboard()
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

player_left = Player((DEFAULT_LEFT, 0))
player_right = Player((DEFAULT_RIGHT, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkeypress(player_left.paddle_up, "e")
screen.onkeypress(player_left.paddle_down, "d")

screen.onkeypress(player_right.paddle_up, "Up")
screen.onkeypress(player_right.paddle_down, "Down")

ball.get_ball_heading()
game_running = True

while game_running:
    time.sleep(0.05)
    screen.update()

    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    # Detect collision with paddle
    elif ball.distance(player_left) < 20 or ball.distance(player_right) < 20:
        ball.paddle_bounce()
        ball.speed(ball.speed()+1)

    ###################Detect scoring
    if ball.xcor() > 390:
        ################score to player left
        scoreboard.point_left_player()
        ball.setpos(0, 0)
        ball.paddle_bounce()
        player_left.setpos(DEFAULT_LEFT, 0)
        player_right.setpos(DEFAULT_RIGHT, 0)

    if ball.xcor() < -390:
       #################score to player right
        scoreboard.point_right_player()
        ball.setpos(0, 0)
        ball.paddle_bounce()
        player_left.setpos(DEFAULT_LEFT, 0)
        player_right.setpos(DEFAULT_RIGHT, 0)



screen.exitonclick()
