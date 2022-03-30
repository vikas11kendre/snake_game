from turtle import Turtle
import random
list_of_colors=["#3DB2FF","#FFB830","#FF2442","#AE00FB","#16C79A"]
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color(random.choice(list_of_colors))
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE : {self.score}", align="center", font=("Arial", 18, "normal"))
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"game over", align="center", font=("Arial", 18, "normal"))

    def score_record(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

