from turtle import Turtle
import random


class Food(Turtle):  # ita means that our Food class is a sort of Turtle
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # these fn are inherited from the Turtle class
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 240)
        self.goto(x=x_axis, y=y_axis)
