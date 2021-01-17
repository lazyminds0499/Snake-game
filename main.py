from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
game_is_on = True
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.back, key="Down")
food = Food()
score = ScoreBoard()
while game_is_on:
    screen.update()  # it happens when all the pieces re moved then the screen is refreshed
    time.sleep(0.1)  # here the sleep fn is used after all pieces have moved
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.score_count()

        # snake.snake_tail()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # for snake to collide with food
        score.reset()
        snake.new_game()

    for turtle in snake.turtles_lst[1:]:
        if snake.head.distance(turtle) < 10:
            score.reset()
            snake.new_game()


screen.exitonclick()