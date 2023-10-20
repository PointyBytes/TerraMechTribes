# TerraMechTribes

## Overview

This is a board game with role-playing elements inspired by a variety of literature, video games, and movies. The game is divided into three main phases:

1. **Base Building**: Players start by building a base, making difficult moral choices that will shape their environment.
2. **Hunting Phase**: Players form hunting parties to go out into the Zone to hunt for dangerous robotic creatures.
3. **Combat Phase**: Engage in tactical battles against AI-driven robotic foes.

## Classes and Files

This project contains several Python files each housing one or more classes. They are as follows:

- `main.py`: Contains the main game loop and orchestrates the game mechanics.
- `board.py`: Manages the `Board` and `Terrain` classes that are used during the `CombatPhase`.
- `entity.py`: Houses the `Survivor` class and potentially shared rules for quarry entities.
- `player.py`: Defines the `Player` class, which holds RPG elements like strength, intelligence, etc.
- `tutorial.py`: Designed for guiding new players through the game mechanics.
- `hunting.py`: Contains the `HuntingPhase` class to manage the hunting phase.
- `combat.py`: Contains the `CombatPhase` and `ActionManager` classes to manage the combat phase.
- `upkeep_phase.py`: Manages tasks and events that happen in the upkeep phase.
- `zone.py`: Defines the properties and behaviors of the Zone.
- `equipment.py`: Manages the various types of equipment that can be used in the game.
- `quarry.py`: Defines the types of quarry that can be hunted, starting with Salamanders.

Each class is designed to encapsulate specific functionalities and attributes, making it easier to manage the game's growing complexity.

## Inspiration

* Kingdom Death: Monster
* Horizon Zero Dawn
* Generation Zero
* Annihilation / The Southern Reach Trilogy
* Roadside Picnic (upcoming inspiration)

## License

This project is licensed under the CC BY-SA 4.0 License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This project was sparked by a contrasting experience within my gaming group—while I found myself deeply enamored with Kingdom Death: Monster (KDM), one of my fellow players expressed a strong dislike for it. Rather than seeing this as a challenge, I took it as inspiration. Initially, the idea was to re-skin KDM with a Sci-Fi setting. However, not wanting to dilute my own enjoyment and exploration of KDM's rich lore, I decided to create something entirely new yet heavily inspired by it. This game is an homage to KDM and other points of inspiration, tailored to engage a broader range of player interests and preferences. It is a journey of digging deep, both into strategic gameplay and into a rich, underlying lore that gradually unfolds.
