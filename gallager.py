import pgzrun
import random

WIDTH = 1200
HEIGHT = 800

Green = (0,255,0)
Blue  = (0,0,255)

Ship =  Actor("ship")
Bug = Actor("bug")

Ship.pos = (WIDTH//2, HEIGHT - 60)

speed = 5
speed_s = 10
bullets = []
enemies = []
enemies.append(Bug)
enemies[-1].x = 10
enemies[-1].y = -100

score = 0

def display_score():
    screen.draw.text(str(score), (150,80))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = Ship.x
        bullets[-1].y = Ship.y - 50

def update():
    global score
    if keyboard.left:
        Ship.x -= speed_s
        if Ship.x <= 0:
            Ship.x  =  0
    if keyboard.right:
        Ship.x += speed_s
        if Ship.x >= WIDTH:
            Ship.x = WIDTH

def draw():
    screen.clear()
    screen.fill("Blue")
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    Ship.draw()
    display_score()

pgzrun.go()