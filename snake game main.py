from g_snake import Snake
from turtle import Screen
import time
from Food import Food
from scoreboard import ScoreBoard
from outline import Outline
from vk import text
list_of_colors=["#3DB2FF","#FFB830","#FF2442","#AE00FB","#16C79A"]

import random
screen=Screen()
screen.setup(700,600)
screen.bgcolor("white")
screen.title("Snake game created by VK")
outline=Outline()
screen.tracer(0)
s=True
snake=Snake()
food=Food()

scoreboard=ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.k,"w")
#text()
while s:
    color=random.choice(list_of_colors)
    screen.update()
    text(color)
    #time.sleep(0.1)
    snake.move()

    #scoreboard.hover()
    if snake.head.distance(food) <15:
        scoreboard.score_record()
        snake.extend()
        food.refresh()
        snake.change(color)

    if snake.head.xcor()> 310 or snake.head.xcor()<-310 or snake.head.ycor()> 270 or snake.head.ycor()<-270:
        scoreboard.game_over()
        s=False
    for i in snake.segments[1:]:
        if snake.head.distance(i)<4:
            scoreboard.game_over()
            s = False


screen.exitonclick()
