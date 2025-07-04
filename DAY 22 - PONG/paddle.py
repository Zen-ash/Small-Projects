from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,pos):
        super().__init__()
        self.create_paddle(pos)
        

        
    def create_paddle(self, pos):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len= 1 , stretch_wid= 5)
        self.penup()
        self.setpos(pos)



    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)       


    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
