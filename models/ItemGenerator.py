class ItemGenerator:
    def __init__(self, production_speed, capacity):
        self.production_speed = production_speed
        self.stock = 0
        self.capacity = capacity

    @property
    def production_speed(self):
        return self._production_speed

    @production_speed.setter
    def production_speed(self, value):
        self._production_speed = value if value >= 0 else 0

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value if value >= 0 else 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value if value >= 0 else 0
