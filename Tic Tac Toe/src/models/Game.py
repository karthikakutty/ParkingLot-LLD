from .board import Board
from .GameStatus import GameStatus



class Game:
    def __init__(self,dimension,players,winning_strategies):
        self.players=players
        self.winning_strategies=winning_strategies
        self.board=Board(dimension)
        self.moves=[]
        self.next_turn=0
        self.winner=None
        self.gameStatus=GameStatus.INPROGRESSED
        self.snapshots=[]
    #@staticmethod
    #def gameBuilder():
    #   return GameBuilder()
