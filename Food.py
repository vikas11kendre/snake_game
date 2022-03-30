from turtle import Turtle
import random
list_of_colors=["#3DB2FF","#FFB830","#FF2442","#AE00FB","#16C79A"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.75,0.75)
        self.color("#F6416C")
        self.speed("fastest")

    def refresh(self):
        random_x=random.randint(-30,270)
        random_y = random.randint(-200, 270)
        self.goto(random_x,random_y)
        self.color(random.choice(list_of_colors))


