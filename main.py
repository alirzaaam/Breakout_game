import turtle
from Paddle import Paddle
from ball import Ball
from bricks import Bricks
from game_notice import GameNotice

import time
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)
screen.listen()

paddle = Paddle((0, -350))
ball = Ball()
gn = GameNotice()

# Bricks
brick1 = Bricks((300, 350))
brick2 = Bricks((150, 350))
brick3 = Bricks((0, 350))
brick4 = Bricks((-150, 350))
brick5 = Bricks((-300, 350))


screen.onkey(paddle.left, 'a')
screen.onkey(paddle.right, 'd')

while True:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    # Detect collusion with wall
    if ball.ycor() > 380:
        ball.bounce_y()

     # loose ball / Game over
    if ball.ycor() < -380:
        gn.message("GAME OVER")
        paddle.reset()
        ball.reset()

    # Detect collusion with paddle
    if ball.distance(paddle) < 45 and ball.ycor() < -330:
        ball.bounce_y()

    # Detect collusion with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    
    # Detect Bricks
    if ball.distance(brick1) < 45 and ball.ycor() > 330:
        brick1.remove()
        ball.bounce_y()
        
    if ball.distance(brick2) < 45 and ball.ycor() > 330:
        brick2.remove()
        ball.bounce_y()

    if ball.distance(brick3) < 45 and ball.ycor() > 330:
        brick3.remove()
        ball.bounce_y()
        
    if ball.distance(brick4) < 45 and ball.ycor() > 330:
        brick4.remove()
        ball.bounce_y()

    if ball.distance(brick5) < 45 and ball.ycor() > 330:
        brick5.remove()
        ball.bounce_y()

    # Win
    if brick1.visibility and brick2.visibility and brick3.visibility and brick4.visibility and brick5.visibility:
        gn.message("YOU WIN")
        paddle.reset()
        ball.reset()



screen.exitonclick()