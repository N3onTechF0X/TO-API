class NotFoundError(Exception):
    def __init__(self, nick: str):
        """
        Исключение, возникающее, когда запрашиваемый объект не найден.

        :param nick: Никнейм или идентификатор объекта, который не был найден.
        :type nick: str
        """
        self.nick = nick
        super().__init__(self.nick)

class RequestError(Exception):
    def __init__(self, status: int):
        """
        Исключение, возникающее при проблемах с запросом или ответом от сервера.

        :param status: HTTP статус код ответа, который указывает на ошибку в запросе или ответе.
        :type status: int
        """
        self.status = status
        super().__init__(self.status)

class RatingsIndexError(Exception):
    def __init__(self, place: int):
        """
        Исключение, возникающее, когда указанный индекс для доступа к данным в рейтинге находится вне допустимого диапазона.

        :param place: Запрошенное место в рейтинге, которое находится вне допустимого диапазона.
        :type place: int
        """
        self.place = place
        super().__init__(self.place)

class InvalidRangeError(Exception):
    def __init__(self, min_value: int, max_value: int):
        """
        Исключение, которое возникает, когда заданный диапазон значений недопустим или некорректен.

        :param min_value: Начальное значение диапазона.
        :type min_value: int
        :param max_value: Конечное значение диапазона.
        :type max_value: int
        """
        self.min_value = min_value
        self.max_value = max_value
        super().__init__((self.min_value, self.max_value))
