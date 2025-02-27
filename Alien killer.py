import pgzrun
import random

TITLE = "Alien Killer"
WIDTH = 700
HEIGHT = 600

message = ""
score = 0
timeLeft = 30

alien = Actor("alien.png")

alien.pos = 50,50

def draw():
    if timeLeft > 0:
        screen.clear()
        screen.fill(color=("red"))
        alien.draw()
        screen.draw.text(message, center = (80,20),color="blue",fontsize=34)
        screen.draw.text(f"Time Left {int(timeLeft)} s", center = (240,20),color="blue",fontsize=34)
        screen.draw.text(f"Score:{score}", center = (390,20),color="blue",fontsize=34)

def place_alien():
    alien.x = random.randint(50,WIDTH -50)
    alien.y = random.randint(50,HEIGHT -50)

def update():
    global timeLeft
    if timeLeft > 0:
        timeLeft-= 1/60
    else:
        timeLeft = 0

def on_mouse_down(pos):
    global message, score
    if alien.collidepoint(pos):
        score += 1
        message = "Good Shot"
        place_alien()
    else:
        message="You Missed"

place_alien()
pgzrun.go()