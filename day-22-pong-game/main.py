# [x] Create the screen
# [x] Create paddle
# [x] Create second paddle
# [x] Create ball and make it move
# [ ] Detect wall and bounce
# [ ] Detect ball and paddle
# [ ] Detect miss paddle
# [ ] Score
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()\

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Missed
    if ball.xcor() > 380:
        ball.reset_position()
        # left player scores
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        # right player scores
        scoreboard.r_point()

screen.exitonclick()