import random
import time

from game.enemy import Enemy
from game.player import Player
from game.location import Location
from game.shop import shop_menu
from game.utils import print_separator, save_game, load_game, get_random_enemy

p = Player()


def battle(player, enemy):
    print(f"Битва начинается! {player.name} против {enemy.name}!")

    while player.is_alive() and enemy.is_alive():
        print("\n--- Новый раунд ---")
        print(f"{player.name}: Здоровье = {player.hp}, Урон = {player.damage}")
        print(f"{enemy.name}: Здоровье = {enemy.hp}, Урон = {enemy.damage}")

        # Показать меню действий
        print("\nВыберите действие:")
        print("1. Атаковать врага")
        print("2. Использовать лечение")
        print("3. Уйти из битвы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Ход игрока
            player.attack(enemy)
            enemy.take_damage(player.damage)
            print(f"{player.name} атакует {enemy.name} и наносит {player.damage} урона!")
            time.sleep(1)
        elif choice == "2":
            # Использовать лечение
            player.heal()
            print(f"{player.name} восстанавливает здоровье!")
            time.sleep(1)
        elif choice == "3":
            # Уйти из битвы
            print(f"{player.name} решает уйти из битвы...")
            if random.random() <= 0.3:
                print(f"{player.name} не смог убежать и получает {enemy.damage} урона!")
                player.take_damage(enemy.damage)
            else:
                print("Битва продолжается!")
                return

        # Ход врага
        enemy.attack(player)
        player.take_damage(enemy.damage)
        print(f"{enemy.name} атакует {player.name} и наносит {enemy.damage} урона!")
        time.sleep(1)

    # Определение победителя
    if player.is_alive():
        print(f"{player.name} побеждает в битве!")
        player.gain_experience(enemy.xp)
        player.earn_money(enemy.money)
    else:
        print(f"{enemy.name} побеждает в битве! {player.name} проигрывает...")
        player.lose_money(enemy.money // 2)

    # Восстановление здоровья игрока после битвы
    player.heal()

    # Сброс текущего врага
    current_enemy = None


def main_menu(player):
    current_enemy = None
    while True:
        print("\n--- Главное меню ---")
        print("1. Посмотреть статистику игрока")
        print("2. Посмотреть статистику текущего врага")
        print("3. Перейти в магазин")
        print("4. Вылечиться")
        print("5. Пойти сражаться")
        print("6. Перейти в другую локацию")
        print("7. Сохранить игру")
        print("8. Выйти из игры")

        choice = input("Ваш выбор: ")

        if choice == '1':
            player.print_stats()
        elif choice == '2':
            if current_enemy is None:
                print("Нет текущего врага.")
            else:
                current_enemy.print_stats()
        elif choice == '3':
            shop_menu(player)
        elif choice == '4':
            heal_player(player)
        elif choice == '5':
            if current_enemy is None:
                print("Нет текущего врага.")
            else:
                battle(player, current_enemy)
        elif choice == '6':
            current_enemy = change_location()
        elif choice == '7':
            save_game(player, current_enemy)
        elif choice == '8':
            print("До новых встреч!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def change_location():
    forest_enemy_list = [
        {
            'name': 'Рудольф',
            'enemy_specific_property': 'Лесной гоблин'
        },
        {
            'name': 'Эдвард',
            'enemy_specific_property': 'Лесной эльф'
        },
        {
            'name': 'Ведьма',
            'enemy_specific_property': 'Лесная ведьма'
        },
    ]

    dungeon_enemy_list = [
        {
            'name': 'Тролль',
            'enemy_specific_property': 'Подземное чудовище'
        },
        {
            'name': 'Большой паук',
            'enemy_specific_property': 'Подземное чудовище'
        },
        {
            'name': 'Адольф-2',
            'enemy_specific_property': 'Подземный эльф'
        },
    ]

    mountains_enemy_list = [
        {
            'name': 'Козёл',
            'enemy_specific_property': 'Горное чудовище'
        },
        {
            'name': 'Бандит',
            'enemy_specific_property': 'Горный бандит'
        },
    ]

    jungles_enemy_list = [
        {
            'name': 'Обезьяна',
            'enemy_specific_property': 'Обезьяна из джунглей'
        },
    ]

    locations = [
        [Location("Лес"), forest_enemy_list],
        [Location("Подземелье"), dungeon_enemy_list],
        [Location("Сибирские горы"), mountains_enemy_list],
        [Location("Джунгли"), jungles_enemy_list]
    ]

    print("\n--- Выберите новую локацию ---")
    for i, location in enumerate(locations, start=1):
        print(f"{i}. {location[0].name}")

    choice = input("Ваш выбор: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(locations):
            new_location = locations[choice - 1]
            enemy = get_random_enemy(new_location[1])
            current_enemy = Enemy(
                player_level=p.level,
                name=enemy.get('name'),
                enemy_class=enemy.get('enemy_specific_property')
            )
            print(f"Вы переместились в локацию: {new_location[0].name}")
            return current_enemy  # Возвращаем нового врага
    except ValueError:
        pass

    print("Неверный выбор. Возвращаемся в главное меню.")
    return None  # Возвращаем None, если выбор неверен


def heal_player(player):
    heal_cost = 5
    print(f'стоимость лечения {heal_cost}')

    if player.money >= heal_cost:
        player.hp += 100
        player.money -= heal_cost
        print("Вы восполнили здоровье на 100 единиц.")
    else:
        print("У вас недостаточно денег.")

    print("Ваше текущее состояние:")
    player.print_stats()
    print_separator()


if __name__ == '__main__':
    p = None
    e = None

    print("Добро пожаловать в игру!")

    choice = input("Выберите действие:\n1. Начать новую игру\n2. Загрузить сохранение\nВаш выбор: ")

    if choice == '1':
        p = Player()
        main_menu(p)
    elif choice == '2':
        p, e = load_game()
        if p is not None and e is not None:
            main_menu(p)
    else:
        print("Неверный выбор. Попробуйте снова.")
