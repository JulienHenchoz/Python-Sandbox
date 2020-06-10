from models.ItemGenerator import ItemGenerator


class Farm(ItemGenerator):
    def __init__(self, production_speed, capacity):
        ItemGenerator.__init__(self, production_speed, capacity)

    def craft(self):
        if self.stock < self.capacity:
            self.stock += self.production_speed

    def update(self):
        self.craft()
