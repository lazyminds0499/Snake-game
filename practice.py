from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Saanp:
    def __init__(self):
        self.turtles = []
        self.snake_head()
        self.head = self.turtles[0]

    def snake_head(self):
        snake_head = Turtle("square")
        snake_head.color("green")
        snake_head.penup()
        snake_head.goto(0, 0)
        self.turtles.append(snake_head)

    def creating_snake(self, posi):
        topu = Turtle("square")
        topu.color("green")
        topu.penup()
        topu.goto(posi)
        self.turtles.append(topu)

    def extend_snake(self):
        self.creating_snake(self.turtles[-1].position())

    def move_body(self):
        for posi in range(len(self.turtles) - 1, 0, -1):
            x_axis = self.turtles[posi - 1].xcor
            y_axis = self.turtles[posi - 1].ycor
            self.turtles[posi].goto(x=x_axis, y=y_axis)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def back(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)