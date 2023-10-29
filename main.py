from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
    scoreboard = Scoreboard()
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
            scoreboard.update_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
            playing = False
            scoreboard.game_over()

        for segment in snake.snake:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                playing = False
                scoreboard.game_over()


def start():
    screen = setup_screen()
    snake = Snake()
    play_game(snake=snake, screen=screen)

    screen.exitonclick()


start()
