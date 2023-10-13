class Paint:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Paint на основе данных о краске.

        :param data: Данные о краске, включая уровень (grade), идентификатор (id), изображение (imageUrl),
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

class PaintsInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса PaintsInfo на основе данных о красках в пользовательском профиле.

        :param data: Список данных о красках.
        :type data: list
        """
        self.paints = [Paint(paint) for paint in data]

        self.favorite_paint = max(self.paints, key=lambda paint: paint.timePlayed)
