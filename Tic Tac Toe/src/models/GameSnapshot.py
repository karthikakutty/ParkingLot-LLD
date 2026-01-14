import copy

class GameSnapshot:
    def __init__(self,game):
        self.board=copy.deepcopy(game.board)
        self.moves=copy.deepcopy(game.moves)
        self.next_turn=game.next_turn
        self.gameStatus=game.gameStatus
        self.winner=game.winner