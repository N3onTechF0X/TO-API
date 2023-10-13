class Supplie:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Supplie на основе данных о расходных материалах (припасах).

        :param data: Данные о расходных материалах, включая идентификатор (id), изображение (imageUrl),
        имя (name) и количество использований (usages).
        :type data: dict
        """
        self.id = data['id']
        self.imageUrl = data['imageUrl']
        self.name = data['name']
        self.usages = data['usages']

class SuppliesInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса SuppliesInfo на основе данных о расходных материалах (припасах) в пользовательском профиле.

        :param data: Список данных о расходных материалах.
        :type data: list
        """
        self.supplies = [Supplie(supplie) for supplie in data]

        self.most_common_supplie = max(self.supplies, key=lambda supplie: supplie.usages)
