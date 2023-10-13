class Present:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Present на основе данных о подарке.

        :param data: Данные о подарке, включая количество (count), изображение (imageUrl),
        имя (name) и идентификатор прототипа (prototypeId).
        :type data: dict
        """
        self.count = data['count']
        self.imageUrl = data['imageUrl']
        self.name = data['name']
        self.prototypeId = data['prototypeId']

class PresentsInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса PresentsInfo на основе данных о подарках в пользовательском профиле.

        :param data: Список данных о подарках.
        :type data: list
        """
        self.presents = [Present(present) for present in data]

        self.most_common_present = max(self.presents, key=lambda present: present.count)
