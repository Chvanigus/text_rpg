class Armor:
    def __init__(self, name, defense, price):
        self.name = name
        self.defense = defense
        self.price = price

    def __str__(self):
        return f'{self.defense}'