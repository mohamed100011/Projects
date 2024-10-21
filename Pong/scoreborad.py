from turtle import Turtle

FONT = ("courier", 80, "normal")
ALIGN = "center"


class Scoreborad(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.updata_score()

    def updata_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1
