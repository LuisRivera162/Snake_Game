from turtle import Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self) -> None:
        self.snake = []
        self.init_snake()
        self.head = self.snake[0]

    def init_snake(self):
        startX = 0
        for i in range(3):
            dot = Turtle()
            dot.penup()
            dot.speed(0)
            dot.shape('square')
            dot.color('white')
            dot.setx(startX)
            startX -= 20
            self.snake.append(dot)


    def move(self): 
        time.sleep(.2)
        for i in  range(len(self.snake)-1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)

    def is_game_over(self):
        return self.head.xcor() >= 300 or \
            self.head.ycor() >= 300 or \
            self.head.xcor() <= -300 or \
            self.head.ycor() <= -300 or \
            self.check_collision_with_self()
    
    def check_collision(self, food: Turtle):        
        return self.head.distance(food) < 5

    def grow(self):
        dot = Turtle()
        dot.penup()
        dot.speed(1)
        dot.shape('square')
        dot.color('white')
        dot.goto(self.snake[-1].pos())
        self.snake.append(dot)

    def check_collision_with_self(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False