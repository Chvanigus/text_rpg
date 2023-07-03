import pickle
import random


def print_separator():
    print("=" * 40)


def save_game(player, enemy):
    data = {
        'player': player,
        'enemy': enemy
    }

    try:
        with open('savegame.dat', 'wb') as file:
            pickle.dump(data, file)
        print("Игра успешно сохранена!")
    except IOError:
        print("Ошибка при сохранении игры.")


def load_game():
    try:
        with open('savegame.dat', 'rb') as file:
            data = pickle.load(file)
        print("Игра успешно загружена!")
        return data['player'], data['enemy']
    except FileNotFoundError:
        print("Файл сохранения не найден.")
    except IOError:
        print("Ошибка при загрузке игры.")

    return None, None


def get_random_enemy(enemy_list: list) -> dict:
    """Возвращает случайного врага из списка врагов."""
    return random.choice(enemy_list)
