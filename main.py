# import time
# import turtle
# from turtle import Screen, Turtle
# import random
# from snake import Snake
#
# from gensim.scripts.segment_wiki import segment
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My snake game")
# screen.tracer(0)
# snake = Snake()
#
# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
#
# starting_positions = [(0,0), (-20,0), (-40,0)]
# segments = []
#
# for positions in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(positions)
#     segments.append(new_segment)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#
#     for segment_num in range(len(segments)-1, 0, -1):
#         new_x= segments[segment_num-1].xcor()
#         new_y = segments[segment_num-1].ycor()
#         segments[segment_num].goto(new_x,new_y)
#     segments[0].forward(20)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# screen.exitonclick()
#

# In main.py

import time

from turtle import Screen
from snake import Snake
from food import Food
from scor_board import Scoreboard

# NOTE: You can remove the unused import below
# from gensim.scripts.segment_wiki import segment

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()

# Set up controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# REMOVE: All the code below this line used to create and move
#         the segments is now handled by the Snake class.
# starting_positions = [(0,0), (-20,0), (-40,0)]
# segments = []
#
# for positions in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(positions)
#     segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update() # Manually update the screen once per loop
    time.sleep(0.1)
    snake.move()
    #detect collision
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collision
    if snake.head.xcor()>280 or snake.head.xcor()<= -280 or snake.head.ycor()>280 or snake.head.ycor()<= -280:
        game_is_on=False
        scoreboard.game_over()

    #tail collision
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

    # REMOVE: All the code below this line is now handled by snake.move()
    # for segment_num in range(len(segments)-1, 0, -1):
    #     new_x= segments[segment_num-1].xcor()
    #     new_y = segments[segment_num-1].ycor()
    #     segments[segment_num].goto(new_x,new_y)
    # segments[0].forward(20)


screen.exitonclick()