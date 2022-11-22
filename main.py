from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
import random 


#Random colors.
def color():
    return random.randint(0,255)

#Setting up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.colormode(255)

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
    time.sleep(0.06)
    snake.move()
    
    #Detect collision with food and walls.
    
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.got_a_point()
        
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        scoreboard.update_scoreboard()
        snake.reset()   

    #Detect collision with tail.
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.update_scoreboard()
            snake.reset()
            
    #Rainbow snake.
    if scoreboard.score >= 10:
        for snake_obj in snake.snakes:
            snake.color = snake_obj.color(color(), color(), color())
           

screen.exitonclick()
        
        
