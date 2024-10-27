from turtle import Turtle, Screen

the_turtle = Turtle()
# the_turtle.shape("turtle")

# # 1(i). Draw a square, remove the repetative codes
# for line in range(4):
#     the_turtle.forward(100)
#     the_turtle.right(90)

# # 1(ii). Draw a square with different color
# the_turtle.color("blue")
# the_turtle.forward(150)
# the_turtle.color("green")
# the_turtle.right(90)
# the_turtle.forward(150)
# the_turtle.color("black")
# the_turtle.right(90)
# the_turtle.forward(150)
# the_turtle.color("red")
# the_turtle.right(90)
# the_turtle.forward(150)


# We can use alias name, like
# import turtle as t
# the_turtle = t.Turtle()


# # 2. Draw a dashed line
# for line in range(10):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown()


# # 3(i). Draw a Triangle
# for line in range(3):
#     the_turtle.forward(100)
#     the_turtle.right(120)

# # 3(ii). Draw a Square
# for line in range(4):
#     the_turtle.forward(100)
#     the_turtle.right(90)

# # 3(iii). Draw a Pentagon
# for line in range(5):
#     the_turtle.forward(100)
#     the_turtle.right(72)

# # 3(iv). Draw a Hexagon
# for line in range(6):
#     the_turtle.forward(100)
#     the_turtle.right(60)

# # 3(v). Draw a Heptagon
# for line in range(7):
#     the_turtle.forward(100)
#     the_turtle.right(51.4287)

# # 3(vi). Draw a Octagon
# for line in range(8):
#     the_turtle.forward(100)
#     the_turtle.right(45)

# # 3(vii). Draw a Nonagon
# for line in range(9):
#     the_turtle.forward(100)
#     the_turtle.right(40)

# # 3(viii). Draw a Decagon
# for line in range(10):
#     the_turtle.forward(100)
#     the_turtle.right(36)

# # 3. Draw all the above structure at once
# from random import choice
# colors = ["red", "blue", "black", "gray", "orange", "green", "yellow"]
# the_turtle.pensize(3)
# def draw_shape(num_of_line):
#     angle = 360 / num_of_line
#     for line in range(num_of_line):
#         the_turtle.forward(100)
#         the_turtle.right(angle)

# for shape_line in range(3, 11):
#     the_turtle.color(choice(colors))
#     draw_shape(shape_line)


# # 4. Draw a random walk
# from random import choice, randint
# import turtle as t

# t.colormode(255)

# def random_color():
#     red = randint(0, 255)
#     blue = randint(0, 255)
#     green = randint(0, 255)
#     the_turtle.pencolor(red, green, blue)

# directions = [0, 90, 180, 270]
# the_turtle.pensize(10)
# the_turtle.speed("fastest")

# for line in range(200):
#     the_turtle.forward(25)
#     random_color()
#     the_turtle.setheading(choice(directions))


# # 5. Draw a Spirograph
# from random import choice, randint
# import turtle as t

# t.colormode(255)
# the_turtle.pensize(3)

# def random_color():
#     red = randint(0, 255)
#     blue = randint(0, 255)
#     green = randint(0, 255)
#     the_turtle.pencolor(red, green, blue)

# def draw_spirograph(gap_size):
#     for line in range(int(360 / gap_size)):
#         random_color()
#         the_turtle.circle(100)
#         the_turtle.speed("fastest")
#         the_turtle.setheading(the_turtle.heading() + gap_size)

# draw_spirograph(10)


# screen = Screen()
# screen.exitonclick()


# # 6. Extract RGB values from an image
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)

# print(rgb_colors)