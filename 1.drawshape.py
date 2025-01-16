import pgzrun
from random import randint
from pygame import Rect

WIDTH = 400
HEIGHT = 400

def draw():
    r = 255
    g = randint(100,255)
    b = 0

    width = WIDTH
    height = HEIGHT - 300

    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center = 200,200
        screen.draw.rect(rect, (r,g,b))

        r-=10
        b += 10

        width -= 10
        height+= 10
pgzrun.go()
