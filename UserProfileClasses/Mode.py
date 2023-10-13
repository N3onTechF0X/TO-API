class Mode:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Mode на основе данных о режиме игры.

        :param data: Данные о режиме игры, включая название (name), заработанные очки (scoreEarned), время игры (timePlayed)
        и тип (type).
        :type data: dict
        """
        self.name = data['name']
        self.scoreEarned = data['scoreEarned']
        self.timePlayed = data['timePlayed']
        self.type = data['type']

class ModesInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса ModesInfo на основе данных о режимах игры в пользовательском профиле.

        :param data: Список данных о режимах игры.
        :type data: list
        """
        self.modes = [Mode(mode) for mode in data]

        self.favorite_mode = max(self.modes, key=lambda mode: mode.timePlayed)
