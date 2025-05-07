from turtle import Turtle


class GameNotice(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-200, 0)
        

    def message(self, msg):
        self.write(msg, font=("Courier", 50, "bold"))
        