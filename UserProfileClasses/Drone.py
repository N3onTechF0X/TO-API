class Drone:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Drone на основе данных о дроне.

        :param data: Данные о дроне, включая уровень (grade), идентификатор (id), изображение (imageUrl),
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

class DronesInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса DronesInfo на основе данных о дронах в пользовательском профиле.

        :param data: Список данных о дронах.
        :type data: list
        """
        self.drones = [Drone(drone) for drone in data]

        self.favorite_drone = max(self.drones, key=lambda drone: drone.timePlayed)
