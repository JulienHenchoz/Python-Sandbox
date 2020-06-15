from enum import Enum
import pygame

from models.TileType import TileType
from utils.MapUtils import MapUtils


class MapManager:
    camera_offset_x = 640
    camera_offset_y = 0
    TILE_WIDTH = 120
    TILE_HEIGHT = 70
    MAP_WIDTH = 16
    MAP_HEIGHT = 16

    def __init__(self, game_manager, asset_manager):
        self.map = [[0 for x in range(self.MAP_WIDTH)] for y in range(self.MAP_HEIGHT)]
        self.game_manager = game_manager
        self.build_empty_map()
        self.asset_manager = asset_manager

    def build_empty_map(self):
        for x in range(len(self.map) - 1):
            for y in range(len(self.map[x]) - 1):
                self.map[x][y] = TileType.GRASS

    def poll_events(self):
        keys = pygame.key.get_pressed()

        # Move camera
        if keys[pygame.K_w]:
            self.camera_offset_y += 15
        elif keys[pygame.K_s]:
            self.camera_offset_y -= 15
        elif keys[pygame.K_a]:
            self.camera_offset_x += 15
        elif keys[pygame.K_d]:
            self.camera_offset_x -= 15

    def draw(self, screen):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                pos_x, pos_y = MapUtils.pos_to_point(
                    (x, y),
                    (self.TILE_WIDTH, self.TILE_HEIGHT),
                    (self.camera_offset_x, self.camera_offset_y)
                )
                if self.map[y][x] == TileType.GRASS:
                    screen.blit(self.asset_manager.assets[TileType.GRASS], (pos_x, pos_y))
                #self.draw_debug_text(screen, x, y)


    def draw_debug_text(self, screen, x, y):
        pos_x, pos_y = MapUtils.pos_to_point(
                    (x, y),
                    (self.TILE_WIDTH, self.TILE_HEIGHT),
                    (self.camera_offset_x, self.camera_offset_y)
                )
        debug_text = str(int(x)) + ", " + str(int(y))
        img = self.asset_manager.fonts["default"].render(debug_text, True, (255, 255, 255))
        screen.blit(img, (pos_x, pos_y + self.TILE_HEIGHT / 3))

