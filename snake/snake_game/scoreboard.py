from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def increase(self):
        super().clear()
        self.score += 1

    def update(self):
        super().write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 200)
        super().write("GAME OVER!", False, "center", ("Arial", 30, "normal"))
