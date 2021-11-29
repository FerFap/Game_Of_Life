from random import randint as ra


class GameOfLife:
    def __init__(self, width, height, cells=100):
        self.game = {}
        self.alive_cells = cells
        self.generate_random(0, 0, width, height)

    def update(self):
        to_update = {}
        for coord in self.game:
            to_update[coord] = 0

        for x, y in self.game:
            to_update[(x + 1, y)] = to_update.get((x + 1, y), 0) + 1
            to_update[(x + 1, y - 1)] = to_update.get((x + 1, y - 1), 0) + 1
            to_update[(x, y - 1)] = to_update.get((x, y - 1), 0) + 1
            to_update[(x - 1, y - 1)] = to_update.get((x - 1, y - 1), 0) + 1
            to_update[(x - 1, y)] = to_update.get((x - 1, y), 0) + 1
            to_update[(x - 1, y + 1)] = to_update.get((x - 1, y + 1), 0) + 1
            to_update[(x, y + 1)] = to_update.get((x, y + 1), 0) + 1
            to_update[(x + 1, y + 1)] = to_update.get((x + 1, y + 1), 0) + 1

        for key, value in to_update.items():
            if (key in self.game) and (value < 2 or value > 3):
                self.game.remove(key)
            elif not (key in self.game) and value == 3:
                self.game.add(key)

    def generate_random(self, start_x, start_y, width, height):
        self.game = {(ra(start_x, start_x + width), ra(start_y, start_y + height)) for _ in range(self.alive_cells)}