class Hull:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Hull на основе данных о корпусе.

        :param data: Данные о корпусе, включая уровень (grade), идентификатор (id), изображение (imageUrl),
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

class HullsInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса HullsInfo на основе данных о корпусах в пользовательском профиле.

        :param data: Список данных о корпусах.
        :type data: list
        """
        self.hulls = [Hull(hull) for hull in data]

        self.favorite_hull = max(self.hulls, key=lambda hull: hull.timePlayed)
