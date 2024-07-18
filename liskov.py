# Класс Bird, который имеет метод fly
class Bird:

    def fly(self):
        print("Эта птица летает")

# Класс Duck, наследующий от Bird, и переопределяющий метод fly
class Duck(Bird):

    def fly(self):
        print("Эта утка летает быстро")

# Функция, принимающая объект, у которого должен быть метод fly
def fly_in_the_sky(animal):
    animal.fly()

# Создаем объекты классов Bird и Duck
b = Bird()
d = Duck()

# Используем функцию fly_in_the_sky для каждого объекта
fly_in_the_sky(b)  # Вывод: Эта птица летает
fly_in_the_sky(d)  # Вывод: Эта утка летает быстро
