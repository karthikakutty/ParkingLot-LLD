from .winning import Winning

class ColWS(Winning):
    def __init__(self):
        self.col_count={}

    def check_winner(self,cell,board):
        symbol=cell.player.symbol
        col=cell.column

        if symbol not in self.col_count:
            self.col_count[symbol]=[0]*board.board_size
        self.col_count[symbol][col]+=1
        return self.col_count[symbol][col]==board.board_size

    def undo_handle(self,cell,board):
        symbol=cell.player.symbol
        self.col_count[symbol][cell.column]-=1