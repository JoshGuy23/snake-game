import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def setup_screen():
    # This function sets up the play screen
    screen = turtle.Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    return screen


def play_game(snake, screen):
    # This function starts the game.
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(turtle.bye, "q")

    playing = True
    while playing:
        # Move the snake
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Update score and regenerate food when eating food
        if snake.head.distance(food) < 15:
            food.generate()
            snake.add_segment()
            scoreboard.update_score()

        # If snake runs into wall, game over.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
            scoreboard.restart()
            snake.reset()

        # If snake runs into tail: game over.
        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.restart()
                snake.reset()


def start():
    # This function is the start of the game.
    screen = setup_screen()
    snake = Snake()
    play_game(snake=snake, screen=screen)

    screen.exitonclick()


start()
