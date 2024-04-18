# 1. Создайте базовый класс `Animal`,
# который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты
# и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Chirp chirp!"

    def fly(self):
        return f"{self.name} is flying."


class Mammal(Animal):
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs

    def make_sound(self):
        return "Growl growl!"

    def run(self):
        return f"{self.name} is running."


class Reptile(Animal):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def make_sound(self):
        return "Hiss hiss!"

    def crawl(self):
        return f"{self.name} is crawling."


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_info(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"Тип: {type(animal).__name__}, Имя: {animal.name}, Возраст: {animal.age}")
        print("\nСотрудники зоопарка:")
        for staff_member in self.staff:
            print(f"Имя: {staff_member.name}, Должность: {type(staff_member).__name__}")

    def add_staff(self, staff):
        self.staff.append(staff)

    def save_zoo(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} is feeding {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} is healing {animal.name}."


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Создание объектов классов
bird = Bird("Parrot", 5, 30)
mammal = Mammal("Lion", 3, 4)
reptile = Reptile("Snake", 2, 60)

# Демонстрация полиморфизма
animal_sound([bird, mammal, reptile])

# Использование композиции для создания зоопарка
zoo = Zoo()

# Добавление животных в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Создание сотрудников зоопарка
keeper = ZooKeeper("John")
vet = Veterinarian("Alice")

# Добавление сотрудников в зоопарк
zoo.add_staff(keeper)
zoo.add_staff(vet)

zoo.display_info()
# Выполнение действий с сотрудниками
print(keeper.feed_animal(bird))
print(vet.heal_animal(mammal))

# Сохраняем состояние зоопарка в файл
zoo.save_zoo("zoo_state.pickle")

# Загружаем состояние зоопарка из файла
loaded_zoo = Zoo.load_zoo("zoo_state.pickle")
loaded_zoo.display_info()