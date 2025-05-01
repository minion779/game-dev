import pgzrun
import random

WIDTH = 900
HEIGHT = 700

centre_x = WIDTH/2
y = 0
centre = (centre_x,y)
font_colour = (255,255,255)
final_level = 6
start_speed = 10
ITEMS = ["Plastic bag", "Battery 1","Battery 2", "Cup","Jar","Chips","Coffee mug"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bg1.png", (0,0))
    if game_over:
        screen.blit("bg2.png", (0,0))
        display_message("Game Over", "Try again")
    elif game_complete:
        screen.blit("bg2.png", (0,0))
        display_message("Well Done!", "You Won!")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(extra_items):
    items_to_create = get_options_tocreate(extra_items)
    mew_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
pgzrun.go()
