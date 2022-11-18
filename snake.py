from turtle import Turtle


MOVE_DISTANCE = 20
STARTING_POS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        
    def create_snake(self):
        for position in STARTING_POS:
            self.new_segment(position)         
        
    def new_segment(self, position):
            snake = Turtle(shape="square")
            snake.color("white") 
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)
            
    def extend(self):
        self.new_segment(self.snakes[-1].position())
            
    def move(self):
        for snake_num in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[snake_num-1].xcor()
            new_y = self.snakes[snake_num-1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
          
    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)
        
    
    
        
    
        