from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.setpos(-100,200)
        self.write(self.left_score, align="center", font=("Arial", 75, "normal"))
        self.setpos(100, 200)
        self.write(self.right_score, align="center", font=("Arial", 75, "normal"))


    def point_left_player(self):
        self.left_score += 1
        self.score_update()

    def point_right_player(self):
        self.right_score += 1
        self.score_update()
