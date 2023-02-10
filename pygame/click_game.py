kirby = Actor('character')
kirby.pos = 250, 50

WIDTH=500
HEIGHT= kirby.height + 20

def draw():
    screen.fill((173, 216, 230))
    kirby.draw()

def update():
    kirby.left = kirby.left + 2
    if kirby.left > WIDTH:
        kirby.right
