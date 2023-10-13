from UserProfileClasses.Drone import DronesInfo
from UserProfileClasses.Hull import HullsInfo
from UserProfileClasses.Mode import ModesInfo
from UserProfileClasses.Mounted import Mounted
from UserProfileClasses.Paint import PaintsInfo
from UserProfileClasses.Present import PresentsInfo
from UserProfileClasses.Rating import Rating
from UserProfileClasses.ResistanceModule import ResistanceModulesInfo
from UserProfileClasses.Supplie import SuppliesInfo
from UserProfileClasses.Turret import TurretsInfo
from UserProfileClasses.Rank import Rank
from UserProfileClasses.Score import Score
from UserProfileClasses.KillsDeaths import KillsDeaths
from UserProfileClasses.Online import Online

class UserProfile:
    def __init__(self, data: dict):
        """
        Инициализирует объект класса UserProfile на основе данных о пользовательском профиле.

        :param data: Данные о пользовательском профиле, включая ранг, статистику, предметы и другие характеристики.
        :type data: dict
        """
        self.rank = Rank(data['rank'])
        self.golds = data['caughtGolds']
        self.kd = KillsDeaths(data['kills'], data['deaths'])
        self.drones = DronesInfo(data['dronesPlayed'])
        self.earned_crystals = data['earnedCrystals']
        self.gs = data['gearScore']
        self.premium = data['hasPremium']
        self.hulls = HullsInfo(data['hullsPlayed'])
        self.modes = ModesInfo(data['modesPlayed'])
        self.mounted = Mounted(data['mounted'])
        self.name = data['name']
        self.paints = PaintsInfo(data['paintsPlayed'])
        self.presents = PresentsInfo(data['presents'])
        self.prev_rating = Rating(data['previousRating'])
        self.rating = Rating(data['rating'])
        self.resistanceModules = ResistanceModulesInfo(data['resistanceModules'])
        self.score = Score(data['score'], data['scoreBase'], data['scoreNext'])
        self.supplies = SuppliesInfo(data['suppliesUsage'])
        self.turrets = TurretsInfo(data['turretsPlayed'])

        self.profile_link = f"https://ratings.tankionline.com/ru/user/{self.name}"
        self.online = Online(data['modesPlayed'])
