from requests import get

from User import UserProfile
from Top import Top
from TestServer import TestServersInfo
from errors import *

__all__ = ['get_profile', 'get_test_servers', 'get_top', 'NotFoundError', 'RequestError', 'RatingsIndexError', 'InvalidRangeError']

async def get_profile(nickname: str) -> UserProfile:
    """
    Получает профиль пользователя по его никнейму.

    :param nickname: Никнейм пользователя.
    :type nickname: str
    :return: Профиль пользователя.
    :rtype: UserProfile
    :raises: RequestError, NotFoundError
    """
    response = get(f"https://ratings.tankionline.com/api/eu/profile?user={nickname}&lang=ru")
    if response.status_code != 200:
        raise RequestError(response.status_code)
    data = response.json()
    if data.get("responseType") == "NOT_FOUND":
        raise NotFoundError(nickname)
    return UserProfile(data["response"])

async def get_top() -> Top:
    """
    Получает топ игроков.

    :return: Топ игроков.
    :rtype: Top
    :raises: RequestError
    """
    response = get("https://ratings.tankionline.com/api/eu/top/")
    if response.status_code != 200:
        raise RequestError(response.status_code)
    return Top(response.json()["response"])

async def get_test_servers() -> TestServersInfo:
    """
    Получает информацию о тестовых серверах.

    :return: Информация о тестовых серверах.
    :rtype: TestServersInfo
    :raises: RequestError
    """
    response = get("https://test.tankionline.com/public_test")
    if response.status_code != 200:
        raise RequestError(response.status_code)
    return TestServersInfo(response.json())
