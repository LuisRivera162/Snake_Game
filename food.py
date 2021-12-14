from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('cyan')
        self.speed(0)
        self.generate_location()

    def generate_location(self):
        random_x = random.randint(-14, 14)
        random_y = random.randint(-14, 12)
        self.goto(random_x * 20, random_y * 20)

    def location(self):
        return (self.xcor(), self.ycor())