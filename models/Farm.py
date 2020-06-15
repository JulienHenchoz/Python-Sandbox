import pygame

from models.ItemGenerator import ItemGenerator


class Farm(ItemGenerator, pygame.sprite.Sprite):
    def __init__(self, position, image, production_speed, capacity):
        ItemGenerator.__init__(self, production_speed, capacity)
        pygame.sprite.Sprite.__init__(self)
        pos_x, pos_y = position
        self.image = image
        self.rect = pygame.Rect(pos_x, pos_y, self.image.get_rect().width, self.image.get_rect().height)

    def craft(self):
        if self.stock < self.capacity:
            self.stock += self.production_speed

    def update(self):
        self.craft()
