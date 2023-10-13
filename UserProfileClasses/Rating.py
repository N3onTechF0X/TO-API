class RatingValue:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса RatingValue на основе данных о значении в рейтинге.

        :param data: Данные о значении в рейтинге, включая позицию (position) и значение (value).
        :type data: dict
        """
        self.position = data['position'] if data else None
        self.value = data['value'] if data else None

class Rating:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Rating на основе данных о рейтинге игрока в различных категориях.

        :param data: Данные о рейтинге, включая категории кристаллов (crystals), эффективности (efficiency),
        золота (golds) и счёта (score).
        :type data: dict
        """
        self.crystals = RatingValue(data['crystals'])
        self.efficiency = RatingValue(data['efficiency'])
        self.golds = RatingValue(data['golds'])
        self.score = RatingValue(data['score'])
