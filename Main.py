import pygame
import pygame.math

from Game import Game

# PYGame Initialisieren
pygame.init()
# Grösse festlegen
game = Game(800, 600)

# Start Loop
game.loop()

# Close the window and quit.
pygame.quit()
