from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("CornflowerBlue")
        self.speed("fastest")
        self.generate()

    def generate(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.setposition(x=x_cord, y=y_cord)
