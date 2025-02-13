import pgzrun
import random

TITLE = "Alien Killer"
WIDTH = 700
HEIGHT = 600

message = ""

alien = Actor("alien.png")

alien.pos = 50,50

def draw():
    screen.clear()
    screen.fill(color=("red"))
    alien.draw()
    screen.draw.text(message, center = (80,20),color="blue",fontsize=34)

def place_alien():
    alien.x = random.randint(50,WIDTH -50)
    alien.y = random.randint(50,HEIGHT -50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot"
        place_alien()  
    else:
        message="You Missed"

place_alien()
pgzrun.go()