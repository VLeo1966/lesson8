from abc import ABC, abstractmethod

# Шаг 1: Создаём абстрактный класс для оружия
class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):

    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):

    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Модифицируем класс Fighter
class Fighter:

    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self):
        return self.weapon.attack()

# Класс Monster, представляющий монстра
class Monster:

    def __init__(self, name):
        self.name = name

    def defeat(self):
        return f"Монстр {self.name} побежден!"

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(f"{fighter.name} выбирает оружие.")
    print(fighter.attack())
    print(monster.defeat())

# Создаём объекты классов и демонстрируем бой
fighter = Fighter("Боец", Sword())
monster = Monster("Дракон")

# Демонстрация боя с мечом
battle(fighter, monster)

# Боец выбирает лук
fighter.change_weapon(Bow())

# Демонстрация боя с луком
battle(fighter, monster)
