import pgzrun
import random

WIDTH=1200
HEIGHT=700

score = 0
over = False

bee = Actor("bee.png")
bee.pos = 600,350
flower = Actor("flower.png")
flower.pos = 900, 600

def draw():
    screen.blit("background.jpg", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score = "+str(score) ,color="black",fontsize=50, topleft=(30,50))
    screen.draw.text

def flower_pos():
    flower.x = random.randint(70, WIDTH - 70)
    flower.y = random.randint(70, HEIGHT - 70)

def update():
    global score
    if keyboard.left:
        bee.x -= 4
    elif keyboard.right:
        bee.x += 4
    elif keyboard.up:
        bee.y += 4
    elif keyboard.down:
        bee.y -= 4

    flowers_collected = bee.colliderect(flower)

    if flowers_collected:
        score += 1
        flower_pos()

pgzrun.go()