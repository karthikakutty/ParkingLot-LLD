from helper.Stratergy.botStgy.BotStgy import BotStgy
from models.CellStatus import CellStatus
from models.board import Board
class Medium(BotStgy):
    def decide_move(self,board):

        #try to win
        winning_cell=self.find_winning_move(board)
        if winning_cell:
            return winning_cell

        #try to block opponent
        blocking_cell=self.find_blockig_move(board)
        if blocking_cell:
            return blocking_cell

        #fallback first empty
        for row in board.grid:
            for cell in row:
                if cell.status==CellStatus.EMPTY:
                    return cell

    #--------helpers-----------------------------
    def find_winning_move(self,board):
        for row in board.grid:
            for cell in row:
                if cell.status==CellStatus.EMPTY:
                    cell.status==CellStatus.FILLED
                    if self.is_winning(board):
                        cell.status=CellStatus.EMPTY
                        return cell
                    cell.status=CellStatus.EMPTY
        return None

    def find_blocking_move(self,board):
        for row in board.grid:
            for cell in row:
                if cell.status==CellStatus.EMPTY:
                    cell.status=CellStatus.FILLED
                    if self.is_winning(board):
                        cell.status=CellStatus.EMPTY
                        return cell
                    cell.status=CellStatus.EMPTY
        return None

    def is_winning(self,board,symbol):
        size=board.board_size

        #rows
        for r in range(size):
            if all(board.grid[r][c].player and board.grid[r][c].player.symbol == symbol for c in range(size)):
                return True

        #column
        for c in range(size):
            if all(board.grid[r][c].player and board.grid[r][c].player.symbol == symbol for r in range(size)):
                return True

        #diagnols
        if all(board.grid[i][i].player and board.grid[i][i].player.symbol == symbol
               for i in range(size)):
            return True

        if all(board.grid[i][size-i-1].player and board.grid[i][size-i-1].player.symbol == symbol for i in range(size)):
            return True

        return False
