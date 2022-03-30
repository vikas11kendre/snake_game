from turtle import Turtle

class Outline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#2D4059")
        self.speed("fastest")
        self.hideturtle()
        self.pensize(5)
        self.penup()
        self.goto(-310,270)
        self.pendown()
        self.goto(-310,-270)
        self.goto(310,-270)
        self.goto(310,270)
        self.goto(-310, 270)

