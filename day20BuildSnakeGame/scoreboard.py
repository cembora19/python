from statistics import mode
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
PATH="C:\\Users\\cembora\\Desktop\\kodlama\\python\\day20BuildSnakeGame\\"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(f"{PATH}data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open(f"{PATH}data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()