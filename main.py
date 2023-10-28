from turtle import Turtle, Screen
# Notes: Turtles are 20 pixels by 20 pixels


def start():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snake")

    snake = []
    x_pos = 0
    for _ in range(3):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(y=0, x=x_pos)
        x_pos -= 20
        snake.append(new_segment)
    screen.exitonclick()


start()
