import pgzrun
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
        satelite = Actor("sateltite.png")
        satelites.pos = (randint(40, WIDTH-40)), (randint(40, HEIGHT-40))
        satelites.append(satelite)
    start_time = time()