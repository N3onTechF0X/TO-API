class Online:
    def __init__(self, modes: list):
        """
        Инициализирует объект класса Online на основе данных о времени онлайн в различных режимах игры.

        :param modes: Список данных о времени онлайн в различных режимах игры.
        :type modes: list
        """
        self.total = sum(mode['timePlayed'] for mode in modes)

        # Рассчитываем количество часов, минут, секунд и миллисекунд
        self.hours, remainder = divmod(self.total, 1000*60*60)
        self.minutes, remainder = divmod(remainder, 1000*60)
        self.seconds, self.milliseconds = divmod(remainder, 1000)
