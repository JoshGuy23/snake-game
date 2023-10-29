from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(260)
        self.color("white")
        self.score = 0
        self.print_score()

    def print_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()
