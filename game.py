import pgzrun
from pgzero.actor import Actor
import pylance
import pygame

# Window Size
WIDTH = 800
HEIGHT = 600

# Actors
bee = Actor("bee")
flower = Actor("flower")

# Setting Initial Positions
bee.pos = (100, 300)
flower.pos = (650, 300)

# Draw Everything
def draw():
    screen.clear()
    screen.fill("skyblue")
    bee.draw()
    flower.draw()

# Keyboard Controls
def update():
    if keyboard.left:
        bee.x-=5
    if keyboard.right:
        bee.x+=5
    if keyboard.up:
        bee.y+=5
    if keyboard.down:
        bee.y-=5
    if bee.colliderect("flower"):
        screen.draw.text("Bee reached the flower!", center = (WIDTH//2, 50), fontsize = 40, color = "red")

# Start
pgzrun.go()