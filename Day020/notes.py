
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

from turtle import Turtle, Screen
import time
# 1. Create a black screen for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

# 2. Create a snake body

segments = []

starting_position = [(0,0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# 3. Update Screen
    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
        
    # 4. Move the snake

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# Control the snake






screen.exitonclick()