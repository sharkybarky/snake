from turtle import Turtle

FONT = ("Arial", 15, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = -1
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.score}",
                   align=ALIGNMENT,
                   font=FONT)

    def game_ended(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)
