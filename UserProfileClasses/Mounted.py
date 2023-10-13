class Mounted:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса Mounted на основе данных о снаряжении, установленном на игрока.

        :param data: Данные о снаряжении, включая броню (armor), окраску (coloring) и оружие (weapon).
        :type data: dict
        """
        self.armor = data['armor']
        self.coloring = data['coloring']
        self.weapon = data['weapon']
