from enum import Enum

import pygame

from models.TileType import TileType


class MenuMode(Enum):
    IDLE = "IDLE"
    ACTIVE = "ACTIVE"


class ItemType(Enum):
    FACTORY = "FACTORY"
    FARM = "FARM"


class MenuItem(pygame.sprite.Sprite):
    def __init__(self, image, original_image, rect):
        pos_x, pos_y = rect
        print(rect)
        pygame.sprite.Sprite.__init__(self)
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

    def __init__(self, asset_manager):
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
                    resized_sprite,
                    sprite,
                    (pos_x, self.menu_pos_y)
                )
            )
            i += 1

    def draw(self, screen):
        if self.selected_item:
            pos_x, pos_y = pygame.mouse.get_pos()
            pos_x -= self.selected_item.original_image.get_rect().width / 2
            pos_y -= self.selected_item.original_image.get_rect().height / 2
            screen.blit(self.selected_item.original_image, (pos_x, pos_y))
        self.menu_sprites.draw(screen)

    def poll_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                for sprite in self.menu_sprites.spritedict:
                    if sprite.rect.collidepoint(pos):
                        self.selected_item = sprite
            elif pygame.mouse.get_pressed()[2]:
                self.selected_item = None

    def resize_to_width(self, sprite, target_width):
        current_width, current_height = sprite.get_rect().size
        ratio = current_width / target_width
        new_width = int(current_width / ratio)
        new_height = int(current_height / ratio)
        return pygame.transform.scale(sprite, (new_width, new_height))




