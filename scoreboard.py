from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.max_score = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High score: {self.max_score}", align="center", font=("arial", 20, "bold"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align="center", font=("aerial", 20, "normal"))

    def reset(self):
        if self.score > self.max_score:
            self.max_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(str(self.max_score))
        self.score = 0
        self.update_scoreboard()

    def score_count(self):
        self.score += 1
        self.update_scoreboard()