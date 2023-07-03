from .weapon import Weapon
from .armor import Armor
from .utils import print_separator


def shop_menu(player):
    print("Магазин:")
    print("1. Купить оружие")
    print("2. Купить броню")
    print("3. Статистика игрока")
    print("4. вернутся обратно")
    print_separator()
    choice = input("Ваш выбор: ")

    if choice == "1":
        show_weapon_menu(player)
    elif choice == "2":
        show_armor_menu(player)
    elif choice == "3":
        player.print_stats()
    elif choice == "4":
        return
    else:
        print("Неверный выбор. Попробуйте снова.")

    print("Ваше текущее состояние:")
    player.print_stats()
    print_separator()


def show_weapon_menu(player):
    available_weapons = {
        1: Weapon("Меч", 20, 19),
        2: Weapon("Лук", 15, 7),
        3: Weapon("Кинжал", 10, 5),
        4: Weapon("Сюрикен", 4, 3),
        5: Weapon("Автомат АК-12", 50, 100),
        6: Weapon("Топор", 23, 13),
        7: Weapon("магический посох", 1000, 1000),
        8: Weapon("СУПЕР МЕГА ПУПЕР ОЧЕНЬ КРУТОЙ МЕЧ ТООООООЧНОООО НЕЕЕЕЕЕ СКААААААМММ", 1,
                  100000000000000000000000000000000000000000000000000000000000000000000000),
        9: Weapon("Копьё", 15, 16)
    }

    print("Доступное оружие:")
    for weapon_id, weapon in available_weapons.items():
        print(f"{weapon_id}. {weapon.name} (Урон: {weapon.damage}) - Цена: {weapon.price} монет")

    print(f"{len(available_weapons) + 1}. Вернуться в магазин")

    choice = input("Ваш выбор: ")

    if choice.isdigit():
        choice = int(choice)
        if choice in available_weapons:
            buy_weapon(player, available_weapons[choice])
            return

    print("Неверный выбор. Попробуйте снова.")

    print("Ваше текущее состояние:")
    player.print_stats()
    print_separator()


def buy_weapon(player, weapon):
    if player.money >= weapon.price:
        player.equip_weapon(weapon.damage)
        player.money -= weapon.price
        print(f"Вы купили {weapon.name}.")
    else:
        print("У вас недостаточно денег.")
    print_separator()


def show_armor_menu(player):
    available_armor = {
        1: Armor("Легкая броня", 5, 8),
        2: Armor("Средняя броня", 10, 12),
        3: Armor("Тяжелая броня", 15, 18),
        4: Armor("СУПЕР ПУПЕР МЕГА КРУТАЯ БРОНЯ", 1, 100000000000000000000000000000000000000000000000000000000),
        5: Armor("Стальная броня", 24, 25),
        6: Armor("Деревянная броня", 7, 9),
        7: Armor("какаято крутая броня", 30, 29),
    }

    print("Доступная броня:")
    for armor_id, armor in available_armor.items():
        print(f"{armor_id}. {armor.name} (Защита: {armor.defense}) - Цена: {armor.price} монет")

    print(f"{len(available_armor) + 1}. Вернуться в магазин")

    choice = input("Ваш выбор: ")

    if choice.isdigit():
        choice = int(choice)
        if choice in available_armor:
            buy_armor(player, available_armor[choice])
            return

    print("Неверный выбор. Попробуйте снова.")

    print("Ваше текущее состояние:")
    player.print_stats()
    print_separator()


def buy_armor(player, armor):
    if player.money >= armor.price:
        player.equip_armor(armor.defense)
        player.money -= armor.price
        print(f"Вы купили {armor.name}.")
    else:
        print("У вас недостаточно денег.")
    print_separator()
