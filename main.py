from turtle import Screen
from snake import Snake
from food import Food
import time


def setup_screen():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    return screen


def play_game(snake, screen):
    food = Food()
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
        if snake.head.distance(food) < 15:
            food.generate()
            snake.add_segment()


def start():
    screen = setup_screen()
    snake = Snake()
    play_game(snake=snake, screen=screen)

    screen.exitonclick()


start()
