import pygame

from manager.AssetManager import AssetManager
from manager.MapManager import MapManager
from manager.MenuManager import MenuManager


class GameManager:

    def __init__(self, screen, fps):
        pygame.init()
        self.screen = screen
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.asset_manager = AssetManager()
        self.menu_manager = MenuManager(self.asset_manager)
        self.map_manager = MapManager(self.asset_manager)

    def poll_events(self):
        for event in pygame.event.get():
            self.map_manager.poll_events()
            self.menu_manager.poll_events(event)
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.clock.tick(self.fps)
        self.poll_events()

        self.screen.fill([0,0,0])
        self.map_manager.draw(self.screen)
        self.menu_manager.draw(self.screen)

        pygame.display.update()

