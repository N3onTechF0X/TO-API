class ResistanceModule:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса ResistanceModule на основе данных о модуле сопротивления.

        :param data: Данные о модуле сопротивления, включая уровень (grade), идентификатор (id), изображение (imageUrl),
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

class ResistanceModulesInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса ResistanceModulesInfo на основе данных о модулях сопротивления в пользовательском профиле.

        :param data: Список данных о модулях сопротивления.
        :type data: list
        """
        self.resistance_modules = [ResistanceModule(resistance_module) for resistance_module in data]

        self.favorite_resistance_module = max(self.resistance_modules, key=lambda resistance_module: resistance_module.timePlayed)
