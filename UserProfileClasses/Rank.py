from config.data import ranks

class Rank:
    def __init__(self, rank: int):
        """
        Инициализирует объект класса Rank на основе данных о ранге пользователя.

        :param rank: Номер ранга.
        :type rank: int
        """
        self.rank = rank

        self.rank_text = f"Легенда {self.rank-30}" if self.rank > 31 else ranks.get(self.rank, "Неизвестный ранг")
        self.rank_img = f"https://raw.githubusercontent.com/N3onTechF0X/shizoval_DiscordBot/main/ranks/{min(self.rank, 31)}.png"
