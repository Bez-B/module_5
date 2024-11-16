class House:

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, no_floors):
        self.name = name
        self.number_of_floors = no_floors
        self.new_floor = None
    #     self.welcome()
    #
    #
    # # Вне задания добавлен метод приветствия для самопроверки
    # def welcome(self):
    #     print(f'Рады приветствовать Вас! Добро пожаловать в новый элитный {self.number_of_floors}-этажный {self.name}')


    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if self.new_floor < 1 or self.new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(self.new_floor):
                print(i + 1)

 # Задание "Специальные методы классов"
    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


# Задание "Нужно больше этажей"
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            print('Ошибка ввода данных: Неверный тип')


    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print('Ошибка ввода данных: Неверный тип')

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
