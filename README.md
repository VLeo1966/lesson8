# lesson8


 Объяснение кода:
Абстрактный класс Weapon:

Создаётся с абстрактным методом attack(), который будет реализован в конкретных классах оружия.
Конкретные типы оружия:

Классы Sword и Bow наследуют Weapon и реализуют метод attack() по-своему.
Класс Fighter:

Имеет атрибут weapon для хранения текущего оружия.
Метод change_weapon() позволяет менять оружие бойца.
Метод attack() вызывает метод attack() текущего оружия.
Класс Monster:

Представляет монстра, с которым боец сражается.
Метод defeat() выводит сообщение о победе над монстром.
Функция battle():

Симулирует бой между бойцом и монстром, используя текущее оружие бойца.
Демонстрация использования кода:

Создаётся объект бойца с мечом и объект монстра.
Демонстрируется бой с мечом.
Затем боец меняет оружие на лук и снова демонстрируется бой.
Этот пример демонстрирует принцип открытости/закрытости: новые типы оружия можно добавлять, просто создавая новые классы, наследующие Weapon, не изменяя существующий код бойцов или механизм боя.
