from .players import Player
from .PlayerType import PlayerType
from helper.Stratergy.winningStgy.BotFactory import BotFactory

class Bot(Player):
    def __init__(self,player_id,name,symbol,difficulty):
        super().__init__(name,player_id,PlayerType.BOT,symbol)
        self.difficulty=difficulty
        self.stgy=BotFactory.getBot(self.difficulty)
        self.stgy.set_symbol(symbol)

    def decide_cell(self,board):
        return self.stgy.decide_move(board)