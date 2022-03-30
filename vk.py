import turtle
import time
import random
screen=turtle.Screen()
screen.setup(700,600)


def text(c):
    eraser = turtle.Turtle()
    eraser.hideturtle()
    def erasableWrite(tortoise, name, font, align, reuse=None):
        eraser.speed("fastest")
        eraser.up()
        eraser.color(c)
        eraser.setposition(tortoise.position())
        eraser.write(name, font=font, align=align)
        return eraser

    t = turtle.Turtle()
    t.hideturtle()

    t.speed("fastest")
    t.hideturtle()
    t.up()
    t.goto(-700,700)
    t.up()
    t.color("blue")
    t.goto(random.randint(-270,270),random.randint(-270,270))
    eraseble = erasableWrite(t, "CREATED BY VK", font=("Arial", 10, "normal"), align="center")
    screen.update()
    time.sleep(0.1)

    eraseble.clear()


'''t.goto(random.randint(-270,270),random.randint(-270,270))
erasable = erasableWrite(t, "erasable", font=("Arial", 20, "normal"), align="center", reuse=eraseble)'''


'''from turtle import Turtle
import random
from turtle import Turtle
import random
class Hover(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.color("#DA0037")
        self.penup()
        self.goto(-300,270)
        self.hideturtle()

    def update_hover(self):
        self.goto(random.randint(-260,260),random.randint(-260,260))
        self.write(f"created by vk ", align="center", font=("Arial", 18, "normal"))'''
