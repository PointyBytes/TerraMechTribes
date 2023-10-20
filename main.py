from board import Board
from entity import Survivor
from equipment import Equipment
from upkeep_phase import UpkeepPhase
from combat import CombatPhase, ActionManager
from player import Player
from quarry import Quarry


def main():
    # Initialize the game state
    players = [Player() for _ in range(4)]  # Example: Create 4 players
    board = Board()
    upkeep_phase = UpkeepPhase()
    combat_phase = CombatPhase()
    action_manager = ActionManager()

    quarry_entities = []  # Populate this list as needed
    game_over = False

    while not game_over:  # Main game loop
        # Example: Upkeep Phase
        for player in players:
            upkeep_phase.run(player)

        # Example: Combat Phase
        for player in players:
            action_manager.movement_action(player, board)
            action_manager.general_action(
                player, board, quarry_entities
            )  # Example: Add quarry_entities as needed

        # Example: Check game over conditions
        # game_over = check_game_over_conditions()

    # Example: End-of-game logic here
    print("Game Over")


if __name__ == "__main__":
    main()
