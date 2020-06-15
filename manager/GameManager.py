import pygame

from manager.AssetManager import AssetManager
from manager.MapManager import MapManager
from manager.MenuManager import MenuManager
from models.Factory import Factory
from models.Farm import Farm
from models.TileType import TileType
from utils.MapUtils import MapUtils


class GameManager:
    map_manager = None
    factories = []

    def __init__(self, screen, fps):
        pygame.init()
        self.screen = screen
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.asset_manager = AssetManager()
        self.menu_manager = MenuManager(self, self.asset_manager)
        self.map_manager = MapManager(self, self.asset_manager)

    def poll_events(self):
        for event in pygame.event.get():
            self.map_manager.poll_events()
            self.menu_manager.poll_events(event)
            if event.type == pygame.QUIT:
                self.running = False

    def create_item(self, menu_item, pos):
        if menu_item.tile_type == TileType.FARM:
            self.factories.append(Farm(
                pos,
                self.asset_manager.assets[TileType.FARM],
                1,
                10
            ))

    def draw_factories(self):
        for factory in self.factories:
            position = MapUtils.pos_to_point(
                (factory.rect.x, factory.rect.y),
                (self.map_manager.TILE_WIDTH, self.map_manager.TILE_HEIGHT),
                (self.map_manager.camera_offset_x, self.map_manager.camera_offset_y)
            )

            self.screen.blit(factory.image, position)

    def update(self):
        self.clock.tick(self.fps)
        self.poll_events()

        self.screen.fill([0, 0, 0])
        self.map_manager.draw(self.screen)
        self.draw_factories()
        self.menu_manager.draw(self.screen)

        pygame.display.update()

