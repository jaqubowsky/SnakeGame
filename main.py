from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

#Setting up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Creating 3-square snake.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Creating snake movement
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

#Updating screen per 0.1 seconds so snake can move using move() function.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food and walls.
    
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.got_a_point()
        
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
           

screen.exitonclick()
        
        
