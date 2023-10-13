class Score:
    def __init__(self, current: int, max_xp: int, min_xp: int):
        """
        Инициализирует объект класса Score на основе данных о текущих, максимальных и минимальных очках.

        :param current: Текущие очки.
        :type current: int
        :param max_xp: Максимальное количество очков.
        :type max_xp: int
        :param min_xp: Минимальное количество очков.
        :type min_xp: int
        """
        self.current = current
        self.max = max_xp
        self.min = min_xp

        # Рассчитываем процент прогресса и оставшееся количество очков
        self.percent = round((self.current-self.min)/(self.max-self.min)*100, 2)
        self.remaining = self.max-self.current
