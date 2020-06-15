from enum import Enum

import pygame

from models.TileType import TileType
from utils.MapUtils import MapUtils


class MenuMode(Enum):
    IDLE = "IDLE"
    ACTIVE = "ACTIVE"


class ItemType(Enum):
    FACTORY = "FACTORY"
    FARM = "FARM"


class MenuItem(pygame.sprite.Sprite):
    def __init__(self, tile_type, image, original_image, rect):
        pos_x, pos_y = rect
        pygame.sprite.Sprite.__init__(self)
        self.tile_type = tile_type
        self.original_image = original_image
        self.image = image
        self.rect = pygame.Rect(pos_x, pos_y, self.image.get_rect().width, self.image.get_rect().height)


class MenuManager:
    menu_pos_x = 25
    menu_pos_y = 25

    item_spacement = 125
    item_width = 100

    menu_items = [TileType.FACTORY, TileType.FARM]
    menu_sprites = pygame.sprite.Group()

    selected_item = None

    def __init__(self, game_manager, asset_manager):
        self.game_manager = game_manager
        self.currentMode = MenuMode.IDLE
        self.asset_manager = asset_manager
        self.create_menu_sprites()

    def create_menu_sprites(self):
        i = 0
        while i < len(self.menu_items):
            item = self.menu_items[i]
            sprite = self.asset_manager.assets[item]
            pos_x = self.menu_pos_x + i * self.item_spacement
            resized_sprite = self.resize_to_width(sprite, self.item_width)
            self.menu_sprites.add(
                MenuItem(
                    item,
                    resized_sprite,
                    sprite,
                    (pos_x, self.menu_pos_y)
                )
            )
            i += 1

    def draw(self, screen):
        if self.selected_item:
            tile_width = self.game_manager.map_manager.TILE_WIDTH
            tile_height = self.game_manager.map_manager.TILE_HEIGHT
            x, y = MapUtils.point_to_pos(
                pygame.mouse.get_pos(),
                (tile_width, tile_height),
                (self.game_manager.map_manager.camera_offset_x, self.game_manager.map_manager.camera_offset_y),
            )
            pos_x, pos_y = MapUtils.pos_to_point(
                (x, y),
                (tile_width, tile_height),
                (self.game_manager.map_manager.camera_offset_x, self.game_manager.map_manager.camera_offset_y),
            )

            pos_y = pos_y - (tile_height / 2)
            pos_x = pos_x + (tile_width / 2 / 3)

            screen.blit(self.selected_item.original_image, (pos_x, pos_y))
        self.menu_sprites.draw(screen)

    def poll_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                tile_size = (self.game_manager.map_manager.TILE_WIDTH, self.game_manager.map_manager.TILE_HEIGHT)
                camera_offset = (
                    self.game_manager.map_manager.camera_offset_x,
                    self.game_manager.map_manager.camera_offset_y
                )
                mouse_position = pygame.mouse.get_pos()
                item_pos = MapUtils.point_to_pos(mouse_position, tile_size, camera_offset)

                for sprite in self.menu_sprites.spritedict:
                    if sprite.rect.collidepoint(mouse_position):
                        self.selected_item = sprite

                if self.selected_item and self.is_in_bounds(item_pos):
                    self.game_manager.create_item(self.selected_item, item_pos)

            elif pygame.mouse.get_pressed()[2]:
                self.selected_item = None

    def is_in_bounds(self, item_pos):
        x_in_bounds = (item_pos[0] >= 0) and (item_pos[0] < self.game_manager.map_manager.MAP_WIDTH)
        y_in_bounds = (item_pos[1] >= 0) and (item_pos[1] < self.game_manager.map_manager.MAP_HEIGHT)
        return x_in_bounds and y_in_bounds


    def resize_to_width(self, sprite, target_width):
        current_width, current_height = sprite.get_rect().size
        ratio = current_width / target_width
        new_width = int(current_width / ratio)
        new_height = int(current_height / ratio)
        return pygame.transform.scale(sprite, (new_width, new_height))




