from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            new_segment = self.create_segment()
            new_segment.setposition(y=0, x=x_pos)
            x_pos -= 20
            self.snake.append(new_segment)

    def create_segment(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        return new_segment

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(20)
