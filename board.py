class Terrain:
    # Centralized dictionary containing terrain types and their properties
    terrain_types = {
        "water": {"size": (2, 4), "movement_cost": 2, "keywords": ["drown"]},
        "shoreline": {"size": (2, 4), "movement_cost": 2, "keywords": []},
        "boulder": {
            "size": (3, 3),
            "movement_cost": 1,
            "keywords": ["climbable", "impassable", "blocks_sight"],
        },
        # ...add more here
    }

    def __init__(self, terrain_type):
        if terrain_type not in Terrain.terrain_types:
            raise ValueError(f"Invalid terrain type: {terrain_type}")

        self.type = terrain_type
        self.size = Terrain.terrain_types[terrain_type]["size"]
        self.movement_cost = Terrain.terrain_types[terrain_type]["movement_cost"]
        self.keywords = Terrain.terrain_types[terrain_type]["keywords"]

    def __str__(self):
        return f"Terrain Type: {self.type}, Size: {self.size}, Movement Cost: {self.movement_cost}, Keywords: {self.keywords}"


class Board:
    def __init__(self, rows=12, columns=12):
        self.rows = rows
        self.columns = columns
        self.board = self.create_board()

    def create_board(self):
        # Example: Terrain('forest', False, True, True)
        return [
            [Terrain("plain", True, False, False) for _ in range(self.columns)]
            for _ in range(self.rows)
        ]

    def display_board(self):
        for row in self.board:
            print([cell.type for cell in row])
