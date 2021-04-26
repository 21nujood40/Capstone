import os
os.system("clear")

import turtle
import time

#Set up the window
wn = turtle.Screen()
wn.title("Mole in the Hole")
wn.bgcolor("light blue")
wn.setup(800, 600)
wn.tracer(0)
 
# Pens
pen_grid = turtle.Turtle()
pen_grid.color("green", "white")
pen_grid.shape("square")

pen_player = turtle.Turtle()
pen_player.color("black")

pen_hole = turtle.Turtle()
pen_hole.color("white")

class Mole():    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.position = "standing"
        
    def go_right(self):
        self.col += 1

    def go_left(self):
        self.col -= 1

    def go_forward(self):
        self.row += 1

    def go_backwards(self):
        self.row -= 1

mole = Mole(1,1)
#Keyboard Bindings
wn.listen() 
wn.onkeypress(mole.go_right, "Right")
wn.onkeypress(mole.go_left, "Left")
wn.onkeypress(mole.go_forward, "Down")
wn.onkeypress(mole.go_backwards, "Up")
   
win = (7,4) 

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

#def stopwatch(t):
    #while t:
        #mins, secs = divmod(t, 60)
        #timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end = "\r")
        #time.sleep(1)
        #t -= 1
        #print ("goodbye")
        
while True:
    print(mole.row, mole.col)
    
    # Is the mole at the winning point
    if mole.row == 4 and mole.col == 7:
        print("Win")
    # Check if the mole is off the grid
    if mole.row ==5 and mole.col == 9 or mole.row == 3 and mole.col <= 0 or mole.row == 4 and mole.col <= 4 or mole.row == 5 and mole.col <= 5 or mole.col == 3 and mole.row <= 0 or mole.col == 4 and mole.row <= 0 or mole.col == 5 and mole.row <= 0 or mole.col == 6 and mole.row <= 1 or mole.col == 7 and mole.row <= 1 or mole.col == 8 and mole.row <= 1 or mole.col == 9 and mole.row <= 2 or mole.row < 0 or mole.row > 5 or mole.col < 0 or mole.col > 9:
        print("Lose")
    
    #stopwatch(5)
    
    # Draw blocks
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            x = -100 + (20 * col)
            y = 40 - (20 * row)
            pen_grid.penup()
            pen_grid.goto(x, y)
            if grid[row][col] == 1:
                pen_grid.color("green")
            elif grid[row][col] == 0:
                pen_grid.color("light blue")
            pen_grid.stamp()
    
    # Draw player
    pen_player.penup()
    x = -100 + (20 * mole.col)
    y = 40 - (20 * mole.row)
    pen_player.goto(x, y)
    pen_player.stamp()
    
    # Draw hole
    pen_hole.penup()
    x = 40
    y = -40 
    pen_hole.goto(x, y)
    pen_hole.stamp()
    
    # move player
    
    wn.update()


wn.mainloop()
