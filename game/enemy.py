from random import randint
from game.weapon import Weapon
from game.armor import Armor


class Enemy:
    def __init__(self, player_level, name: str, enemy_class: str,):
        self.name = name if name else None
        self.enemy_class = enemy_class if enemy_class else None
        self.level = player_level
        self.hp = randint(70, 130) * self.level
        self.damage = randint(6, 13) * self.level
        self.xp = randint(5, 10) * self.level
        self.money = randint(1, 10) * self.level
        self.weapon = Weapon("Оружие врага", self.damage, self.level * 2)
        self.armor = Armor("Броня врага", self.level * 5, self.level * 3)

    def equip_weapon(self, weapon_damage):
        self.damage += weapon_damage
        self.weapon = weapon_damage
        print(f"Враг экипировал оружие с уроном {weapon_damage}.")

    def equip_armor(self, armor_points):
        self.armor += armor_points
        print(f"Враг экипировал броню с {armor_points} защитными очками.")

    def attack(self, player):
        player.take_damage(self.damage)
        print(f"Враг атаковал вас и нанес {self.damage} урона.")

    def take_damage(self, damage):
        if damage > 0:
            self.hp -= damage
            print(f"Враг получил {damage} урона.")
            if self.hp <= 0:
                print("Враг побежден!")
        else:
            print("Броня врага поглощает весь урон.")

    def print_stats(self):
        print(f"Имя врага: {self.name}")
        print(f"Класс врага: {self.enemy_class}")
        print(f"Уровень: {self.level}")
        print(f"Здоровье: {self.hp}")
        print(f"Урон: {self.damage}")
        print(f"Опыт: {self.xp}")
        print(f"Монеты: {self.money}")
        print(f"Броня: {self.armor}")

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False
