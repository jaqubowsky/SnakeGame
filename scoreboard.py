from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font = FONT)
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT, font = FONT)
            
            
    def got_a_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    
        

        
        
        
        
        