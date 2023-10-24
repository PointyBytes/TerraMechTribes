# Quarry class represents the general behavior and attributes of quarry (monsters) in the game.
class Quarry:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.ai_deck = []  # Initialize AI deck to be empty
        # TODO: Add more attributes like HP, attack power, etc.


# Salamander class inherits from Quarry and represents the specific behaviors and attributes of a Salamander.
class Salamander(Quarry):
    common_hunt_cards = [
        "Easy Track",
        "Ambush",
        "Water Hazard",
        "Deadly Trap",
    ]  # common to all ages
    hunt_track = [  # Changed from salamander_hunt_track to make it more general
        "general",
        "specific",  # Changed from "salamander" to "specific"
        "specific",  # Changed from "salamander" to "specific"
        "general",
        "boss",  # Changed from "salamander_boss" to "boss"
    ]  # Just an example

    def __init__(self, name, difficulty, age):
        super().__init__(name, difficulty)
        self.age = age  # Age can be "young", "adult", or "elder"

        # Initialize AI deck and hunt cards based on Salamander's age
        self.initialize_ai_deck()
        self.specific_hunt_cards = []  # Initialize the specific hunt cards
        self.initialize_hunt_cards()

        # Example terrain setup
        self.terrain_setup = [
            {"type": "water", "position": (0, 0)},
            {"type": "shoreline", "position": (2, 0)},
            # TODO: Add more terrain types and their positions.
        ]

    def set_encounter_distance(self):
        if self.age == "young":
            self.encounter_distance = 3
        elif self.age == "adult":
            self.encounter_distance = 5
        else:  # elder
            self.encounter_distance = 7

    def initialize_ai_deck(self):
        """Initialize the AI deck based on the Salamander's age."""
        base_attacks = ["Charge", "Tail Swipe"]
        if self.age == "young":
            self.ai_deck = base_attacks + ["Slime"]
        elif self.age == "adult":
            self.ai_deck = base_attacks + ["Slime", "Death Roll"]
        else:  # elder
            self.ai_deck = base_attacks + ["Slime", "Death Roll", "Whirlpool"]

    def initialize_hunt_cards(self):
        """Initialize the specific hunt cards based on the Salamander's age."""
        # TODO: Implement logic for initializing hunt cards based on age

    # TODO: Implement Salamander-specific actions like "Death Roll", "Whirlpool", etc.
    def death_roll(self, target):
        """Perform a Death Roll attack on the target."""
        pass  # TODO: Implement the logic here

    def whirlpool(self, target):
        """Perform a Whirlpool attack on the target."""
        pass  # TODO: Implement the logic here
