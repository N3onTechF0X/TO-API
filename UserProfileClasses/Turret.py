class Turret:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Turret на основе данных о башне (туррелье).

        :param data: Данные о башне, включая уровень (grade), идентификатор (id), изображение (imageUrl),
        имя (name), характеристики (properties), заработанные очки (scoreEarned) и время игры (timePlayed).
        :type data: dict
        """
        self.grade = data['grade']
        self.id = data['id']
        self.imageUrl = data['imageUrl']
        self.name = data['name']
        self.properties = data['properties']
        self.scoreEarned = data['scoreEarned']
        self.timePlayed = data['timePlayed']

class TurretsInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса TurretsInfo на основе данных о башнях (туррельях) в пользовательском профиле.

        :param data: Список данных о башнях (туррельях).
        :type data: list
        """
        self.turrets = [Turret(turret) for turret in data]

        self.favorite_turret = max(self.turrets, key=lambda turret: turret.timePlayed)
