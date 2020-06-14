import pygame
from manager.GameManager import GameManager

screen = pygame.display.set_mode((1280, 960))
gameManager = GameManager(screen, 60)

while gameManager.running:
    gameManager.update()
