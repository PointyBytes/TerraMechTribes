# TerraMechTribes

## Overview

This is a board game with role-playing elements inspired by Kingdom Death: Monster (KDM), Frostpunk, and potentially Maze Runner. The game is divided into three main phases:

1. **Base Building**: Players start by building a base, making difficult moral choices that will shape their environment.
2. **Hunting Phase**: Players form hunting parties to go out into the Zone to hunt for dangerous robotic creatures.
3. **Combat Phase**: Engage in tactical battles against AI-driven robotic foes.

## Classes and Files

This project contains several Python files each housing one or more classes. They are as follows:

- `main.py`: Contains the main game loop and orchestrates the game mechanics.
- `entity.py`: Houses the `Survivor` class and potentially shared rules for quarry entities.
- `player.py`: Defines the `Player` class, which holds RPG elements like strength, intelligence, etc.
- `tutorial.py`: Designed for guiding new players through the game mechanics.
- `phases.py`: Contains `HuntingPhase` and `CombatPhase` classes to manage different game phases.
- `upkeep_phase.py`: Manages tasks and events that happen in the upkeep phase.
- `zone.py`: Defines the properties and behaviors of the Zone.
- `equipment.py`: Manages the various types of equipment that can be used in the game.
- `quarry.py`: Defines the types of quarry that can be hunted, starting with Salamanders.

Each class is designed to encapsulate specific functionalities and attributes, making it easier to manage the game's growing complexity.

## License

This project is licensed under the CC BY-SA 4.0 License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Inspired by games like Kingdom Death: Monster, Frostpunk, The Monster Hunter series, and potentially Maze Runner.

