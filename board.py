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
    def __init__(self, size=12):
        self.size = size
        self.board = self.initialize_board()

    def initialize_board(self):
        """Initialize a board with '-' representing empty squares."""
        return [["-" for _ in range(self.size)] for _ in range(self.size)]

    def board_to_string(self):
        """Convert the board to a string representation."""
        return "\n".join([" ".join(row) for row in self.board])

    def display(self):
        """Display the board."""
        print(self.board_to_string())


# Example usage:
if __name__ == "__main__":
    my_board = Board()
    my_board.display()
