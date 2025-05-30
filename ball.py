from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = -4
        self.y_move = -4
        self.move_speed = 0.02

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)


    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 0.1

    def bounce_x(self):
        self.x_move *= -1
        

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()