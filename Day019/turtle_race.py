from turtle import Turtle, Screen
from random import randint

is_race_on = False

screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "blue", "green", "purple", "black"]
y_positions = [-60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 5):
    the_turtle = Turtle(shape="turtle")
    the_turtle.color(colors[turtle_index])
    the_turtle.penup()
    the_turtle.goto(x=-250, y=y_positions[turtle_index])
    all_turtles.append(the_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for new_turtle in all_turtles:
        if new_turtle.xcor() > 270:
            is_race_on = False
            winning_color = new_turtle.pencolor()
            if winning_color == user_bet:
                print(f" You have won. The {winning_color} turtle is winner.")
            else:
                print(f" You lost. The {winning_color} turtle is winner.")

        random_distance = randint(0, 10)
        new_turtle.forward(random_distance)


screen.exitonclick()