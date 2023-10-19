improvised_weapons = {
    "Branch": {
        "activation_icon": "Some_Symbol",
        "speed": 1,
        "accuracy": 7,
        "strength": "Some_Value",
        "keywords": ["bludgeoning", "fragile"],
    },
    "Snapped Bone": {
        "activation_icon": "Another_Symbol",
        "speed": 2,  # Or perhaps faster as you said
        "accuracy": 8,
        "strength": "Another_Value",
        "keywords": ["piercing", "fragile"],
    }
    # Additional weapons can be added here
}


class Equipment:
    def __init__(self, name, bonuses):
        self.name = name
        self.bonuses = bonuses  # Exempel: {'attack': 2, 'defense': 1}
