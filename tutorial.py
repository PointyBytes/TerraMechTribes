from upkeep_phase import BaseBuilding
from equipment import Equipment
from combat import HuntingPhase, CombatPhase, UpkeepPhase
from player import Player
from quarry import Quarry  # Importing the base Quarry class


class Tutorial:
    def __init__(self):
        self.players = []  # List of Player objects
        self.current_phase = (
            None  # Could be an instance of CombatPhase, UpkeepPhase, etc.
        )

    def start_tutorial(self):
        print("Welcome to the Tutorial!")
        self.print_opening_scene()
        # Additional initialization logic here, such as creating Player objects and setting the starting scene

    def print_opening_scene(self):
        print("------------------------------------------------------")
        print("You wake up in a glade, bordering a bayou-like environment.")
        print(
            "Disoriented, with no memory of who you are, the silence around you is suddenly shattered."
        )
        print(
            "A deep groaning noise fills the air. A gigantic salamander bursts from the water."
        )
        print(
            "In a flash, it grabs one of the newly awakened individuals, pulling them into the depths."
        )
        print("Screams of panic and pain fill the air.")
        print(
            "You hear the groaning again, closer this time. You don't want to share that fate."
        )
        print(
            "Frantically, you search the ground for anything to defend yourself with."
        )
        print("------------------------------------------------------")

    # ... rest of the code

    def run_combat_phase(self):
        print("Entering Combat Phase...")
        self.current_phase = CombatPhase()
        # Logic for combat phase here

    def run_upkeep_phase(self):
        print("Entering Upkeep Phase...")
        self.current_phase = UpkeepPhase()
        # Logic for upkeep phase here

    def end_tutorial(self):
        print("Tutorial Complete!")
        # Logic for ending the tutorial and transitioning to the main game


if __name__ == "__main__":
    tutorial = Tutorial()
    tutorial.start_tutorial()
    tutorial.run_combat_phase()
    tutorial.run_upkeep_phase()
    tutorial.end_tutorial()
