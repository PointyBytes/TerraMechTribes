import random


class Player:
    def __init__(
        self,
        strength=1,
        intelligence=1,
        dexterity=1,
        gender="Unknown",
        will_points=1,
        max_will_points=1,
    ):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.gender = gender
        self.movement = 5  # Base movement of 5
        self.will_points = will_points  # For rerolls and extra actions
        self.max_will_points = max_will_points  # Maximum limit for will_points
        self.current_position = (0, 0)  # Using (x, y) coordinates for position

    def add_will_points(self, points):
        """
        Adds will points up to the maximum limit.
        """
        self.will_points = min(self.will_points + points, self.max_will_points)

    def move(self, new_position):
        """
        Move the player to a new position on the board.
        """
        # Validate the move is within the allowed movement range.
        # Update the current_position.
        pass

    def take_action(self, action_type):
        """
        Take an action such as attack, dodge, etc.
        """
        # Implement the action here.
        # Use stats like strength, intelligence, etc., to determine the action's outcome.
        pass

    @classmethod
    def create_offspring(cls, parent1, parent2):
        """
        Create an offspring Player object based on two parent Player objects.
        """
        # Check if parents are of opposite genders
        if parent1.gender == parent2.gender:
            print("Parents must be of opposite genders to create an offspring.")
            return None

        # Calculate the new stats based on the parents' stats.
        new_strength = (parent1.strength + parent2.strength) // 2
        new_intelligence = (parent1.intelligence + parent2.intelligence) // 2
        new_dexterity = (parent1.dexterity + parent2.dexterity) // 2

        # Gender is randomly picked for the offspring.
        new_gender = random.choice(["Male", "Female"])

        return cls(
            strength=new_strength,
            intelligence=new_intelligence,
            dexterity=new_dexterity,
            gender=new_gender,
        )
