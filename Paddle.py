from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.color('white')
        self.penup()
        self.goto(position)

    def left(self):
        if self.xcor() > -305:
            self.backward(50)

    def right(self):
        if self.xcor() < 305:
            self.forward(50)

