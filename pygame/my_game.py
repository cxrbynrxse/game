WIDTH=400
HEIGHT=400
score=0
game_over= False

kirby= Actor("character")
kirby.pos= 100, 100

coin= Actor("coin")
coin.pos= 200, 200

from random import randint
def draw():
    screen.fill("light blue")
    kirby.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
        screen.fill("light green")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        kirby.x = kirby.x - 3
    elif keyboard.right:
        kirby.x = kirby.x + 3
    elif keyboard.up:
        kirby.y = kirby.y - 3
    elif keyboard.down:
        kirby.y = kirby.y + 3

    coin_collected = kirby.colliderect(coin)
    if coin_collected:
        score = score + 10
        place_coin()

clock.schedule(time_up, 30.0)
place_coin()
