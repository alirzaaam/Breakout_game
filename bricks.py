from turtle import Turtle


class Bricks(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.color("red")
        self.penup()
        self.goto(position)
        self.visibility = False

    def remove(self):
        self.reset()
        self.visibility = True
        return self.visibility