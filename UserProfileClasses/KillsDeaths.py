class KillsDeaths:
    def __init__(self, kills: int, deaths: int):
        """
        Инициализирует объект класса KillsDeaths на основе данных о количестве убийств и смертей.

        :param kills: Количество убийств.
        :type kills: int
        :param deaths: Количество смертей.
        :type deaths: int
        """
        self.kills = kills
        self.deaths = deaths

        # Рассчитываем соотношение убийств к смертям, округляя до двух знаков после запятой.
        self.kd = round(self.kills/(self.deaths or 1), 2)
