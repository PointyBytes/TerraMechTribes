class Quarry:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.ai_deck = []


class Salamander(Quarry):
    def __init__(self, name, difficulty):
        super().__init__(name, difficulty)
        self.terrain_setup = [
            {"type": "water", "position": (0, 0)},
            {"type": "shoreline", "position": (2, 0)},
            # ... add more here
        ]
