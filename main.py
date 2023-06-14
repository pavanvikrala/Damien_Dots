from turtle import Turtle, Screen
import random

chitti = Turtle()
screen = Screen()
screen.colormode(255)

# I'm importing the colorgram library to extract colors from an image and store them as RGB values in a list called rgb_colors.
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for i in colors :
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)

# Code to print the paiting done by "Damien Hirst"
colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
chitti.speed(0)
chitti.penup()
chitti.goto(-400,-300)

for i in range(1, 281) :
    chitti.dot(20, random.choice(colors))
    chitti.penup()
    chitti.fd(50)

    if i%20 == 0 :
        chitti.seth(90)
        chitti.fd(50)
        chitti.seth(180)
        chitti.fd(1000)
        chitti.seth(0)

screen.exitonclick()
