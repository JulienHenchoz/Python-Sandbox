import pygame

from models.ItemGenerator import ItemGenerator


class Factory(ItemGenerator, pygame.sprite.Sprite):
    def __init__(self, production_speed, capacity):
        ItemGenerator.__init__(self, production_speed, capacity)
        self.raw_materials = 0

    def craft(self):
        if self.raw_materials > 0 and self.stock < self.capacity:
            self.stock += self.production_speed
            self.raw_materials -= 1

    def update(self):
        self.craft()

    @property
    def raw_materials(self):
        return self._raw_materials

    @raw_materials.setter
    def raw_materials(self, value):
        self._raw_materials = value if value >= 0 else 0
