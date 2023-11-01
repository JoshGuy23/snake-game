from turtle import Turtle

# These constants determine the snake's bearing and movement speed.
MOVE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        # This function initializes the snake with 3 segments.
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        # This function creates the initial snake.
        x_pos = 0
        for _ in range(3):
            new_segment = self.create_segment()
            new_segment.setposition(y=0, x=x_pos)
            x_pos -= 20
            self.snake.append(new_segment)

    def add_segment(self):
        # This function adds a new segment to the snake.
        new_segment = self.create_segment()
        tail = self.snake[-1]
        new_segment.setposition(x=tail.xcor(), y=tail.ycor())
        self.snake.append(new_segment)

    def create_segment(self):
        # This function creates a new segment to be added to the snake.
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        return new_segment

    def move(self):
        # This function determines how the snake moves.
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)

    def right(self):
        # This function is used to turn the snake right.
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        # This function is used to turn the snake up.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        # This function is used to turn the snake left.
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        # This function is used to turn the snake down.
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
