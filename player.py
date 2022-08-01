from turtle import Turtle

MOVE_DIST = 20
LEFT_DEFAULT = -350
RIGHT_DEFAULT = 350

class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.turtlesize(5,1)
        self.pu()
        self.goto(position)

    #Move paddle up
    def paddle_up(self):
        new_ycord = self.ycor() + MOVE_DIST
        self.setpos(self.xcor(), new_ycord)

    #Move paddle down
    def paddle_down(self):
        new_ycord = self.ycor() - MOVE_DIST
        self.setpos(self.xcor(), new_ycord)



