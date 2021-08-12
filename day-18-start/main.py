from turtle import Screen
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0)





# ########### Challenge 5 - Spirograph ########
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# def draw_spirograph(size_of_gap):
#     for _ in range( int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(200)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)


# ########### Challenge 4 - Random Walk ########
# turtle.colormode(255)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# tim.speed(0)
# tim.pensize(10)
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(50)
#     tim.setheading(random.choice(directions))
#
#
########### Challenge 3 - Drawing ########
# tim.shape = "circle"
# tim.color("pink")
#
# # tim.pu()
# # tim.backward(200)
# #
# # for _ in range(10):
# #     tim.pd()
# #     tim.forward(20)
# #     tim.pu()
# #     tim.forward(20)
#
# for side in range(3, 11):
#     angle = 360 / side
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(angle)

screen = Screen()
screen.exitonclick()


