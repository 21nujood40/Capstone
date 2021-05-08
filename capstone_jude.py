import os
os.system("clear")

import turtle
import time

#Set up the window
wn = turtle.Screen()
wn.title("Worm in the Hole")
turtle.bgpic("intro.gif") 
turtle.update()
time.sleep(9)
wn.setup(800, 600)
wn.tracer(0)
wn.register_shape("grass.gif")
wn.register_shape("hole.gif")


wn.bgpic("sky.gif")


# Pens
pen_grid = turtle.Turtle()
pen_grid.color("light blue")
pen_grid.shape("square")

pen_player = turtle.Turtle()
pen_player.color("pink")
pen_player.shape("square")

pen_hole = turtle.Turtle()
pen_hole.shape("hole.gif")

class Mole():    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.position = "standing"
        self.center = "center"
        
    def go_right(self):
        if self.position == "standing":
            self.position = "right"
            self.center = "left"
            self.col += 1
            
        elif self.position == "left":
            if self.center == "left":
                self.col += 2
            else:
                self.col += 1
            self.position = "standing"
            self.center = "center"
        
        elif self.position == "right":
            if self.center == "left":
                self.col += 2
            else:
                self.col += 1
            self.position = "standing"
            self.center = "center"

        elif self.position == "up" or self.position == "down":
            self.col += 1
        

    def go_left(self):
        if self.position == "standing":
            self.position = "left"
            self.center = "right"
            self.col -= 1
        
        elif self.position == "right":
            if self.center == "right":
                self.col -= 2
            else:
                self.col -= 1
            self.position = "standing"
            self.center = "center"
        
        elif self.position == "left":
            if self.center == "right":
                self.col -= 2
            else:
                self.col -= 1
            self.position = "standing"
            self.center = "center"
        
        elif self. position == "up" or self.position == "down":
            self.col -= 1


    def go_up(self):
        if self.position == "standing":
            self.position = "up"
            self.row -= 1
        
        elif self.position == "down":
            self.position = "standing"
            self.row -= 1
        
        elif self.position == "right":
            self.row -= 1
        
        elif self. position == "left" or self.position == "right":
            self.row -= 1
            self.position = "standing"
        
        elif self.position == "up":
            self.position = "standing"
            self.row -= 1
        
        

    def go_down(self):
        if self.position == "standing":
            self.position = "down"
            self.row += 1
        elif self.position == "left" or self.position == "right":
            self.row += 1
        elif self.position == "down":
            self.row += 2
            self.position = "standing"
        elif self.postion == "up":
            self.row += 1
            self.position = "standing"
            


    def render(self, pen):
        pen.penup()
        x = -100 + (20 * self.col)
        y = 40 - (20 * self.row)
        pen.goto(x, y)
        pen.color("pink")
        pen.stamp()
        
        row = self.row
        col = self.col
        
        if self.position == "up":
            row -= 1
            
        elif self.position == "down":
            row += 1    
        elif self.position == "right":
            col += 1
        elif self.position == "left":
            col -= 1
            
            
        pen.penup()
        x = -100 + (20 * col)
        y = 40 - (20 * row)
        pen.goto(x, y)
        pen.color("pink")
        pen.stamp()
            
        


mole = Mole(1,1)
#Keyboard Bindings
wn.listen() 
wn.onkeypress(mole.go_right, "Right")
wn.onkeypress(mole.go_left, "Left")
wn.onkeypress(mole.go_down, "Down")
wn.onkeypress(mole.go_up, "Up")
   
win = (7,4) 
score = ""

#Create grid
grid = [
    [1,1,1,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,1,2,1,1],
    [0,0,0,0,0,0,1,1,1,0]
    
]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        print(grid[row][col], end="")
    print("") 


        
while True:
    print(mole.row, mole.col)
    
    # Is the mole at the winning point
    if mole.row == 4 and mole.col == 7 and mole.position == "standing":
        score = "Win"
    # Check if the mole is off the grid
    if grid[mole.row][mole.col] == 0:
        score = "Lose"
        
    if mole.position == "left" and grid[mole.row][mole.col-1] == 0:
        score = "Lose"
    elif mole.position == "right" and grid[mole.row][mole.col+1] == 0:
        score = "Lose"
   
    
    
    # Draw blocks
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = -100 + (20 * col)
            y = 40 - (20 * row)
            pen_grid.penup()
            pen_grid.goto(x, y)
            if grid[row][col] == 1:
                pen_grid.shape("grass.gif")
            elif grid[row][col] == 0:
                pen_grid.shape("square")
            pen_grid.stamp()
    
    # Draw player
    mole.render(pen_player)
    
    # Draw hole
    pen_hole.penup()
    x = 40
    y = -40 
    pen_hole.goto(x, y)
    pen_hole.stamp()
    
    if score == "Lose":
        turtle.bgpic("lose.gif") 
        turtle.update()
        time.sleep(3)
        exit()
    elif score =="Win":
        turtle.bgpic("win.gif")  
        turtle.update()
        time.sleep(3)
    wn.update()


wn.mainloop()
