from turtle import Turtle , Screen
import time
import random
from vk import text
positions_list=[(0,0),(-20,0),(-40,0)]
#from color_picker import ColorImagePickerList
#k=ColorImagePickerList("color.png",3)
#color_list=k.image_color_list
class Snake:

    def __init__(self):
        self.segments= []
        self.create_snake()
        self.head=self.segments[0]

    def k (self):
        s = True
    def create_snake(self):
        for position in positions_list:
            self.add_segment(position)

    def add_segment(self,position):
            turtle =Turtle("square")
            turtle.color("#00B8A9")
            turtle.penup()
            turtle.goto(position)
            self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range (len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def change(self,colorSnake):
        for i in self.segments:
            i.color(colorSnake)


    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def left (self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

