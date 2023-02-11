from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.fail = "GAME OVER"
        self.level_up()

    def level_up(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def update_level(self):
        self.score += 1
        self.level_up()

    def game_over(self):
        self.goto(0, 0)
        self.write(self.fail, align="center", font=FONT)