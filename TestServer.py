class TestServer:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса TestServer на основе данных о тестовом сервере.

        :param data: Данные о тестовом сервере, включая релиз, домен, URL и количество пользователей.
        :type data: dict
        """
        self.release = data['Release']
        self.domain = data['Domain']
        self.url = data['Url']
        self.user_count = data['UserCount']

        self.number = int(self.release.replace('deploy', '')[0])
        self.link = f"https://public-deploy{self.number}.test-eu.tankionline.com/browser-public/index.html?config-template=https://c{{server}}.public-deploy{self.number}.test-eu.tankionline.com/config.xml&resources=../resources&balancer=https://balancer.public-deploy{self.number}.test-eu.tankionline.com/balancer"

class TestServersInfo:
    def __init__(self, data: list):
        """
        Инициализирует объект класса TestServersInfo на основе данных о тестовых серверах.

        :param data: Список данных о тестовых серверах.
        :type data: list
        """
        self.test_servers = [TestServer(value) for value in data]

        self.popular_server = max(self.test_servers, key=lambda test_server: test_server.user_count)

    async def is_server_open(self, number: int) -> bool:
        """
        Проверяет, открыт ли тестовый сервер с указанным номером.

        :param number: Номер тестового сервера.
        :type number: int
        :return: True, если сервер открыт, иначе False.
        :rtype: bool
        """
        return any(test_server.number == number for test_server in self.test_servers)

    async def get_by_number(self, number: int) -> TestServer:
        """
        Получает информацию о тестовом сервере по его номеру.

        :param number: Номер тестового сервера.
        :type number: int
        :return: Информация о сервере или None, если сервер не найден.
        :rtype: TestServer or None
        """
        return next((test_server for test_server in self.test_servers if test_server.number == number), None)
