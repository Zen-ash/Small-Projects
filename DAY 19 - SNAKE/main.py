from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")





game_is_on  = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    
    snake.move()
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() <-290:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        # if snake.head == segment:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()