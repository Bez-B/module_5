class UrTube:
    """
    Класс базы данных пользователей и видеороликов
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password):
        if self.nickname not in ur.users:





class Video:
    """
    Класс видеороликов, содержащий название, продолжительность, секунду остановки, ограничение по возрасту
    """

#     videos = []
#
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = duration
        self.time_now = int(time_now)
        self.adult_mode = adult_mode


class User:
    """
    Класс пользователей, содержащий имя пользователя, пароль, возраст
    """

    # users = []
    # current_user = None

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


#
#     def register(self, nickname, password, age):
#         if self.nickname not in ur.users:
#             print('нет такого пользователя надо его добавить')
#             # ur.users
#         else:
#             print(f"Пользователь {self.nickname} уже существует")
#
#
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')