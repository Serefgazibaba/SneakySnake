import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def game_start():
    s = Screen()
    s.setup(width=600, height=600)
    s.bgcolor("black")
    s.title("SNEAKY SNAKE")
    s.tracer(0)
    snake = Snake()
    food = Food()
    score_board = Scoreboard()
    s.listen()
    s.onkey(fun=snake.up, key="Up")
    s.onkey(fun=snake.down, key="Down")
    s.onkey(fun=snake.left, key="Left")
    s.onkey(fun=snake.right, key="Right")

    is_game_on = True

    while is_game_on:

        s.update()
        time.sleep(0.1)
        snake.move_forward()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_board.increase()
            score_board.update()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            is_game_on = False
            score_board.game_over()

        for segments in snake.snake[1:]:
            if snake.head.distance(segments) < 10:
                is_game_on = False
                score_board.game_over()

    key = s.textinput("TRY AGAIN", "Play again ? enter any key.")
    if key:
        s.resetscreen()
        game_start()
    else:
        s.bye()


game_start()
