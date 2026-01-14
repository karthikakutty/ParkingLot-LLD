from .winning import Winning

class RowWS(Winning):

    def __init__(self):
        self.row_count={}

    def check_winner(self,cell,board):
        symbol=cell.player.symbol
        row=cell.row

        if symbol not  in self.row_count:
            self.row_count[symbol]=[0]*board.board_size

        self.row_count[symbol][row]+=1
        return self.row_count[symbol][row]== board.board_size

    def undo_handle(self,cell,board):
        symbol=cell.player.symbol
        self.row_count[symbol][cell.row]-=1