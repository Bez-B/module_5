class House:
    def __init__(self, name, no_floors):
        self.name = name
        self.number_of_floors = no_floors
        self.new_floor = None
        self.welcome()


    # Вне задания добавлен метод приветствия для самопроверки
    def welcome(self):
        print(f'Рады приветствовать Вас! Добро пожаловать в новый элитный {self.number_of_floors}-этажный {self.name}')


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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
