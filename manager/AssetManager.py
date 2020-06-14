import pygame
from models.TileType import TileType


class AssetManager:
    fonts = {}
    assets = {}

    def __init__(self):
        self.fonts["default"] = pygame.font.SysFont("arial", 10)
        self.assets[TileType.GRASS] = pygame.image.load("assets/isometric/grass.png").convert_alpha()
        self.assets[TileType.FACTORY] = pygame.image.load("assets/isometric/factory.png").convert_alpha()
        self.assets[TileType.FARM] = pygame.image.load("assets/isometric/farm.png").convert_alpha()