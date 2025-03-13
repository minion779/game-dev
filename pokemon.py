import pgzrun

WIDTH=1200
HEIGHT=700

ash = Actor("ash.png")
ash.pos = 600,350
pikachu = Actor("pikachu.png")
pikachu.pos = 900, 600

def draw():
    screen.blit("bg.jpg", (0,0))
    ash.draw()
    pikachu.draw()

def update():
    pass
pgzrun.go()