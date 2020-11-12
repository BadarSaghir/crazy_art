import random

import colorgram
from turtle import Screen, colormode, Turtle

# colors = colorgram.extract('img/hertz.jpg', 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print()
colormode(255)
colours = [(238, 232, 86), (201, 159, 103), (176, 12, 60), (112, 175, 203), (31, 112, 158), (158, 86, 41),
           (176, 163, 33), (212, 133, 165), (8, 29, 65), (132, 179, 151), (170, 52, 95), (220, 61, 102), (233, 230, 5),
           (36, 130, 79), (69, 9, 46), (10, 48, 28), (233, 72, 47), (235, 164, 192), (70, 22, 6), (70, 166, 95),
           (23, 42, 131), (30, 166, 201), (142, 27, 17), (133, 213, 230), (16, 93, 55), (12, 86, 99)]
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)


def move_now(angle, steps, dot=False):
    turtle.setheading(angle)
    if dot:
        turtle.dot(15, random.choice(colours))
    turtle.forward(steps)


def draw_dot_line():
    move_now(90, 40)
    move_now(180, 400)
    for i in range(0, 10):
        move_now(0, 40, True)


def crazy_art(rows):
    for i in range(1, 2*rows+1):
        if i <= 10:
            turtle.dot(15, random.choice(colours))
            turtle.forward(40)
        else:
            draw_dot_line()


crazy_art(10)




screen = Screen()
screen.exitonclick()
