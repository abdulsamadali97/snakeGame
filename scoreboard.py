from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write("GAME OVER", True, ALIGNMENT, FONT)