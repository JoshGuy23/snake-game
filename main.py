from turtle import Turtle, Screen
import time
# Notes: Turtles are 20 pixels by 20 pixels


def setup_screen():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    return screen


def create_segment():
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    return new_segment


def play_game(snake, screen):
    playing = True
    while playing:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(snake) - 1, 0, -1):
            new_x = snake[seg_num - 1].xcor()
            new_y = snake[seg_num - 1].ycor()
            snake[seg_num].goto(new_x, new_y)
        snake[0].forward(20)


def start():
    screen = setup_screen()
    snake = []
    x_pos = 0
    for _ in range(3):
        new_segment = create_segment()
        new_segment.setposition(y=0, x=x_pos)
        x_pos -= 20
        snake.append(new_segment)
    play_game(snake=snake, screen=screen)

    screen.exitonclick()


start()
