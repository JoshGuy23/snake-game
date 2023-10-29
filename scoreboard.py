from turtle import Turtle

# These constants determine the text alignment and font settings for the scoreboard
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        # This function initializes the scoreboard.
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(260)
        self.color("white")
        self.score = 0
        self.print_score()

    def print_score(self):
        # This function prints the score.
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        # This function prints the game over message.
        self.sety(0)
        self.write(arg="Game Over", align=ALIGN, font=FONT)

    def update_score(self):
        # This function updates the score.
        self.score += 1
        self.clear()
        self.print_score()
