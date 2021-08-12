from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Betting time", prompt="Who you got?")

colors = ["red", "orange", "yellow", "green", "purple", "blue"]
all_turtles = []
y_positions = -125

# for turtle_index in range(0, 6):
#     tims.append(Turtle(shape="turtle"))
#     tims[turtle_index].penup()
#     tims[turtle_index].color(colors[turtle_index])
#     tims[turtle_index].goto(x=-230, y=y_positions)
#     y_positions += 50

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions)
    y_positions += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()