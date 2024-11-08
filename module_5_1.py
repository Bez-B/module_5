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



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)