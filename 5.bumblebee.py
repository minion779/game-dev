import pgzrun

WIDTH=1200
HEIGHT=700

bee = Actor("bee.png")
bee.pos = 600,350
flower = Actor("flower.png")
flower.pos = 900, 600

def draw():
    screen.blit("background.jpg", (0,0))
    bee.draw()
    flower.draw()
pgzrun.go()