from abc import ABC,abstractmethod

class BotStgy(ABC):

    def __init__(self):
        self.symbol=None

    def set_symbol(self,symbol):
        self.symbol=symbol

    @abstractmethod
    def decide_move(self,board):
        pass