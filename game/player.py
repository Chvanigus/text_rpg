class Player:
    def __init__(self):
        self.name = "Петя"
        self.hp = 100
        self.damage = 10
        self.xp = 0
        self.money = 4
        self.armor = 0
        self.weapon = 0
        self.level = 1

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.damage += 5
        print(f"Поздравляем! Вы достигли уровня {self.level}.")

    def equip_weapon(self, weapon_damage):
        self.damage += weapon_damage
        self.weapon = weapon_damage
        print(f"Вы экипировали оружие с уроном {weapon_damage}.")

    def equip_armor(self, armor_points):
        self.armor += armor_points
        print(f"Вы экипировали броню с {armor_points} защитными очками.")

    def attack(self, enemy):
        enemy.hp -= self.damage
        print(f"Вы атаковали врага и нанесли {self.damage} урона.")

    def take_damage(self, damage):
        damage -= self.armor
        if damage > 0:
            self.hp -= damage
            print(f"Вы получили {damage} урона.")
            if self.hp <= 0:
                print("Вы погибли.")
        else:
            print("Ваша броня поглощает весь урон.")

    def earn_money(self, amount):
        self.money += amount
        print(f"Вы получили {amount} монет.")

    def gain_experience(self, amount):
        self.xp += amount
        print(f"Вы получили {amount} опыта.")

    def print_stats(self):
        print(f"Уровень: {self.level}")
        print(f"Опыт: {self.xp}")
        print(f"Здоровье: {self.hp}")
        print(f"Урон: {self.damage}")
        print(f"Монеты: {self.money}")
        print(f"Броня: {self.armor}")
        print(f"Оружие: {self.weapon}")

    def heal(self):
        self.hp += 50
        print(f"{self.name} вылечился на 50 хп")

    def lose_money(self,money):
        self.money -= money
        print(f"{self.name} потерял {money} монет")
