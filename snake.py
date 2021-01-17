from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]    # we creating all these constants so that later if wanna tweak our
MOVE_DISTANCE = 20                       # snake we could do it easily

# turtle functions work with tuples reminder ******
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.turtles_lst = []
        self.making_snake()
        self.head = self.turtles_lst[0]  # we have made a separate variable for head position square
        # self.x = 40

    def making_snake(self):
        for posi in POSITIONS:
            self.add_snake(posi)

    def add_snake(self, posi):
        turtles = Turtle("square")
        turtles.penup()
        turtles.color("white")
        turtles.goto(posi)
        self.turtles_lst.append(turtles)

    def extend_snake(self):
        self.add_snake(self.turtles_lst[-1].position())

    def move(self):
        for index in range(len(self.turtles_lst) - 1, 0, -1):
            x_axis = self.turtles_lst[index - 1].xcor()
            y_axis = self.turtles_lst[index - 1].ycor()
            self.turtles_lst[index].goto(x_axis, y_axis)
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

    # def snake_tail(self):
    #     posi = (self.x+20, 0)
    #     turtles = Turtle("square")
    #     turtles.penup()
    #     turtles.color("white")
    #     turtles.goto(posi)
    #     self.turtles_lst.append(turtles)

    def new_game(self):
        for i in self.turtles_lst:
            i.goto(1000, 1000)
        self.turtles_lst.clear()
        self.making_snake()
        self.head = self.turtles_lst[0]


