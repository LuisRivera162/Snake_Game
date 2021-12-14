from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='w', fun=snake.move_up)
screen.onkey(key='a', fun=snake.move_left)
screen.onkey(key='s', fun=snake.move_down)
screen.onkey(key='d', fun=snake.move_right)

not_finished = True
while not_finished:
    screen.update()
    snake.move()

    if snake.is_game_over():
        not_finished = False
        scoreboard.game_over()
    
    if snake.check_collision(food):
        food.generate_location()
        scoreboard.score_point()
        snake.grow()
    
screen.exitonclick()