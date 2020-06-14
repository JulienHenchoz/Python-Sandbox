from unittest import TestCase

import pygame

from manager.MenuManager import MenuManager
from models.Farm import Farm


class TestMenuManager(TestCase):
    def test_resize_to_width(self):
        menu_manager = MenuManager(None)
        pygame.display.set_mode((1280, 960))
        sprite = pygame.image.load("../assets/isometric/factory.png").convert_alpha()
        result = menu_manager.resize_to_width(sprite, 100)
        self.assertEqual(result.get_rect().size, (100, 86))