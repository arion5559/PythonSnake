import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def check_hit(snake):
    hit_wall = False
    distance = 295
    if snake.segments[0].xcor() > distance:
        hit_wall = True
    elif snake.segments[0].xcor() < -distance:
        hit_wall = True
    elif snake.segments[0].ycor() > distance:
        hit_wall = True
    elif snake.segments[0].ycor() < -distance:
        hit_wall = True
    return hit_wall


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    if check_hit(snake):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
