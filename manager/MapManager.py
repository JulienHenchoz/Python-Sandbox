from enum import Enum
import pygame

from models.TileType import TileType


class MapManager:
    camera_offset_x = -200
    camera_offset_y = 500
    TILE_WIDTH = 120
    TILE_HEIGHT = 70
    map = [[0 for x in range(16)] for y in range(16)]

    def __init__(self, asset_manager):
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
            for x in range(len(self.map[y]) - 1, -1, -1):
                pos_x, pos_y = self.pos_to_point(x, y)
                if self.map[y][x] == TileType.GRASS:
                    screen.blit(self.asset_manager.assets[TileType.GRASS], (pos_x, pos_y))
                self.draw_debug_text(screen, x, y)


    def pos_to_point(self, x, y):
        return (
                (x * self.TILE_WIDTH / 2) + (y * self.TILE_WIDTH / 2) + self.camera_offset_x,
                (y * self.TILE_HEIGHT / 2) - (x * self.TILE_HEIGHT / 2) + self.camera_offset_y
        )

    def draw_debug_text(self, screen, x, y):
        pos_x, pos_y = self.pos_to_point(x, y)
        debug_text = str(int(x)) + ", " + str(int(y))
        img = self.asset_manager.fonts["default"].render(debug_text, True, (255, 255, 255))
        screen.blit(img, (pos_x, pos_y + self.TILE_HEIGHT / 3))

