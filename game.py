import pgzrun
import pgzero.screen

# Window Size
WIDTH = 800
HEIGHT = 600

# Actors
bee1 = Actor("bee", (280, 345))
flower1 = Actor("flower", (100, 245))

# Draw Everything
def draw():
    screen.clear()
    screen.fill("skyblue")
    bee1.draw()
    flower1.draw()

# Keyboard Controls
def update():
    if keyboard.left:
        bee1.x-=5
    if keyboard.right:
        bee1.x+=5
    if keyboard.up:
        bee1.y-=5
    if keyboard.down:
        bee1.y+=5
    if bee1.colliderect(flower1):
        print("Bee reached the flower!")

# Start
pgzrun.go()
