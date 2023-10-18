class Survivor:
    def __init__(self, x, y, orientation, player):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.player = player  # The Player object

    def move(self, dx, dy):
        # Calculate the new position using `dx` and `dy`.
        new_x = self.x + dx
        new_y = self.y + dy

        # Here we can use the movement points from the Player object.
        if self.player.movement > 0:
            self.x = new_x
            self.y = new_y
            self.player.movement -= 1
        else:
            print("No more movement points left!")

    def apply_stat_modifier(self, stat, value):
        # Example method that uses Player's stats to apply modifiers
        if hasattr(self.player, stat):
            setattr(self.player, stat, getattr(self.player, stat) + value)

    def action(self, action_type):
        # Delegate the action to the Player's `take_action` method
        self.player.take_action(action_type)
