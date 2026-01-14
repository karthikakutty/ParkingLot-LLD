from helper.Stratergy.botStgy.Easy import Easy
from helper.Stratergy.botStgy.Medium import Medium
from helper.Stratergy.botStgy.Hard import Hard
from models.BotDifficulty import BotDifficulty


class BotFactory:
    @staticmethod
    def getBot(difficulty):
        if difficulty ==BotDifficulty.EAZY:
            return Easy()

        if difficulty==BotDifficulty.MEDIUM:
            return Medium()

        if difficulty==BotDifficulty.HARD:
            return Hard()


