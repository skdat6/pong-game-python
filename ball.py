from turtle import Turtle
from player import Player
import random
MOVE_Y = 10
MOVE_X = 10
MOVE_DIST = 10
CIRCLE_RADIUS = 360


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.speed("slow")
        self.pu()
        self.goto(position)
        self.speed("slow")
        self.orientation = random.randint(0, 270)

        self.move_y = MOVE_Y
        self.move_x = MOVE_X

    def get_ball_heading(self):
      checked = False
      while not checked:
        if self.orientation != 90 and self.orientation != 270:
            self.setheading(self.orientation)
            checked = True
        else:
            continue



    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    #Handle ball bounce on wall/ceiling
    def wall_bounce(self):
        self.move_y *= -1

    #Handle ball bounce on paddle
    def paddle_bounce(self):
        self.move_x *= -1