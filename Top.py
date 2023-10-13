from typing import List

from config.data import ranks
from errors import RatingsIndexError, NotFoundError, InvalidRangeError

class Top:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Top на основе данных рейтинга.

        :param data: Данные рейтинга, включая колонки crystals, efficiency, golds и score.
        :type data: dict
        """
        self.crystals = Column(data['crystals'])
        self.efficiency = Column(data['efficiency'])
        self.golds = Column(data['golds'])
        self.score = Column(data['score'])

class UserInColumn:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса UserInColumn на основе данных пользователя в колонке рейтинга.

        :param data: Данные пользователя, включая информацию о ранге, никнейме и других характеристиках.
        :type data: dict
        """
        self.hasPremium = data['hasPremium']
        self.rank = data['rank']
        self.uid = data['uid']
        self.value = data['value']

        self.rank_text = f"Легенда {self.rank-30}" if self.rank > 31 else ranks[self.rank]
        self.rank_img = f"https://raw.githubusercontent.com/N3onTechF0X/TO_API/main/config/ranks/{min(self.rank, 31)}.png"

class Column:
    def __init__(self, data: list):
        """
        Инициализирует объект класса Column на основе данных колонки рейтинга.

        :param data: Данные колонки рейтинга, включая информацию о пользователях.
        :type data: list
        """
        self.users = [UserInColumn(values) for values in data]

    async def get_place(self, place: int) -> UserInColumn:
        """
        Получает информацию о пользователе, занимающем определенное место в колонке рейтинга.

        :param place: Место пользователя в рейтинге (от 1 до 100).
        :type place: int
        :return: Информация о пользователе.
        :rtype: UserInColumn
        :raises: RatingsIndexError
        """
        if place < 1 or place > 100: raise RatingsIndexError(place)
        return self.users[place-1]

    async def get_by_name(self, nickname: str) -> UserInColumn:
        """
        Получает информацию о пользователе по его никнейму.

        :param nickname: Никнейм пользователя.
        :type nickname: str
        :return: Информация о пользователе.
        :rtype: UserInColumn
        :raises: NotFoundError
        """
        if len(nickname) < 4 or len(nickname) > 20: raise NotFoundError(nickname)
        for user in self.users:
            if user.uid == nickname: return user
        raise NotFoundError(nickname)

    async def get_range(self, min_value: int, max_value: int) -> List[UserInColumn]:
        """
        Получает диапазон пользователей в колонке рейтинга.

        :param min_value: Начальное место в рейтинге (от 1 до 100).
        :type min_value: int
        :param max_value: Конечное место в рейтинге (от 1 до 100).
        :type max_value: int
        :return: Список пользователей в заданном диапазоне.
        :rtype: List[UserInColumn]
        :raises: RatingsIndexError, InvalidRangeError
        """
        if min_value >= max_value: raise InvalidRangeError(min_value, max_value)
        if min_value < 1 or min_value > 100: raise RatingsIndexError(min_value)
        if max_value < 1 or max_value > 100: raise RatingsIndexError(max_value)
        return self.users[min_value-1: max_value-1]
