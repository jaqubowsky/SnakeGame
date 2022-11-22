from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as highscore:
            self.highscore = int(highscore.read())
        self.goto(0, 260)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(str(self.highscore))
        self.score = 0
            
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGMENT, font = FONT)
            
    def got_a_point(self):
        self.score += 1
        self.update_scoreboard()
        
    
        

        
        
        
        
        