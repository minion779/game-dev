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
ITEMS = ["plasticbag", "battery1","battery2", "cup","jar","chips","coffeemug"]
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
    items_to_create = get_option_to_create(extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(extra_items):
    items_to_create = ["box"]
    for i in range(extra_items):
        selected_items = random.choice(ITEMS)
        items_to_create.append(selected_items)
    return items_to_create  

def create_items(items_to_create):
    new_items = []
    for options in items_to_create:
        item = Actor(options +  "img")
        new_items.append(item)
    return new_items

def layout_items(item_to_layout):
    number_of_gaps = len(item_to_layout) + 1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(item_to_layout)
    for index, item in enumerate(item_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = start_speed - current_level
        item.anchor = ("center", "bottom")
        animation = animate(item, duration = duration, on_finished = handle_game_over)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global  items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "box" in item.image:
                handle_game_complete()
            else: 
                handle_game_over()

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animation(animations)
    if current_level == final_level:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animation(animation_to_stop):
    for animation in animation_to_stop:
        if animation.running:
            animation.stop()
        
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize = 90, center = (centre_x, y + 50), color = "red")
    screen.draw.text(sub_heading_text, fontsize = 65, center = (centre_x, y + 150), color = "red")



        


pgzrun.go()




