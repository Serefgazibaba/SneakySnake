from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        for _ in range(3):
            position = (-20 * _, 0)
            self.add_segment(position)
        self.head = self.snake[0]

    def add_segment(self, position):
        new_sq = Turtle(shape="square")
        new_sq.color("white")
        new_sq.penup()
        new_sq.goto(position)
        self.snake.append(new_sq)

    def extend(self):
        self.add_segment((self.snake[-1].xcor() * len(self.snake), self.snake[-1].ycor() * len(self.snake)))

    def move_forward(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
