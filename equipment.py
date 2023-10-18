improvised_weapons = {
    "Branch": {
        "activation_icon": "Some_Symbol",
        "speed": 1,
        "accuracy": 7,
        "strength": "Some_Value",  # To be determined
    }
    # Additional weapons can be added here
}


class Equipment:
    def __init__(self, name, bonuses):
        self.name = name
        self.bonuses = bonuses  # Exempel: {'attack': 2, 'defense': 1}
