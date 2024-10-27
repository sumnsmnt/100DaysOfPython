import turtle as t
from random import choice

the_turtle = t.Turtle()
t.colormode(255)
the_turtle.speed("fastest")
the_turtle.penup()
the_turtle.hideturtle()
color_list = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), 
              (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), 
              (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69), 
              (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), 
              (88, 157, 92), (78, 153, 164), (195, 78, 72), (45, 74, 78), 
              (80, 74, 44), (162, 201, 218), (58, 126, 122), (218, 176, 187), 
              (169, 207, 170), (220, 181, 168)]


the_turtle.setheading(225)
the_turtle.forward(300)
the_turtle.setheading(0)
num_of_dots = 100

for color_dot in range(1, num_of_dots + 1):
    the_turtle.dot(25, choice(color_list))
    the_turtle.forward(50)
    if color_dot % 10 == 0:
        the_turtle.setheading(90)
        the_turtle.forward(50)
        the_turtle.setheading(180)
        the_turtle.forward(500)
        the_turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()