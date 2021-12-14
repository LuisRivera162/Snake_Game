from turtle import Turtle

FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=FONT)

    def score_point(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over.', align='center', font=FONT)


