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

#create the player
#player = turtle.Turtle()
#player.color("brown")
#player.shape("turtle")
#player.speed(0)
#player.penup() #remove line
#player.setheading(90) #direction of pic
#player.dx = 0


class Player():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.position = "standing"
        
    def go_right():
        pass
    def go_left():
        pass
    def go_forward():
        pass
    def go_backwards():
        pass

#Keyboard Bindings
wn.listen() 
wn.onkeypress(Player(go_right), "Right")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_forward, "Down")
wn.onkeypress(go_backwards, "Up")
        
player = Player(1,1)

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


wn.mainloop()
