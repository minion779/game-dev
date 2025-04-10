import pgzrun
from time import time
from random import randint

WIDTH = 800
HEIGHT = 600

satelites = []
lines = []
Next_Satelite = 0
start_time = 0
total_time = 0
end_time = 0
num_satelites = 8

# function to create satelite

def create_satelites():
    global start_time
    for i in range(0,num_satelites):
        satelite = Actor("satelite.png")
        satelite.pos = (randint(40, WIDTH-40)), (randint(40, HEIGHT-40))
        satelites.append(satelite)
    start_time = time()

def draw():
    global total_time
    screen.blit("space.png", (0,0))
    numbers = 1
    for satelite in satelites:
        screen.draw.text(str(numbers), (satelite.pos[0]+50, satelite.pos[1]+30), fontsize=34, color="white")
        satelite.draw()
        numbers += 1
    for line in lines: 
        screen.draw.line(line[0], line[1], "yellow")
    
    if Next_Satelite < num_satelites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30,color="white")
    else:
        screen.blit("leaves.jpg",(0,0))
        screen.draw.text("Good Job",(50,150),fontsize=40,color="black")
        screen.draw.text(str(round(total_time,1)),(100,300),fontsize=30,color="black")

def on_mouse_down(pos):
    global Next_Satelite, lines
    if Next_Satelite < num_satelites:
        if satelites[Next_Satelite].collidepoint(pos):
            if Next_Satelite:
                lines.append((satelites[Next_Satelite-1].pos, satelites[Next_Satelite].pos))
            Next_Satelite += 1
        else:
            lines = []
            Next_Satelite = 0

def update():
    pass

create_satelites()

pgzrun.go()