# Main.py

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# turtle_1 = Turtle(shape="square")
# turtle_1.goto(0,0)
# turtle_1.color("white")

# turtle_2 = Turtle(shape="square")
# turtle_2.goto(-20,0)
# turtle_2.color("white")

# turtle_3 = Turtle(shape="square")
# turtle_3.goto(-40,0)
# turtle_3.color("white")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()