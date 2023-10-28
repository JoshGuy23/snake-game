from turtle import Screen
from snake import Snake
import time
# Notes: Turtles are 20 pixels by 20 pixels


def setup_screen():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    return screen


def play_game(snake, screen):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")

    playing = True
    while playing:
        screen.update()
        time.sleep(0.1)
        snake.move()


def start():
    screen = setup_screen()
    snake = Snake()
    play_game(snake=snake, screen=screen)

    screen.exitonclick()


start()
