from helper.Stratergy.botStgy.BotStgy import BotStgy
from models.CellStatus import CellStatus



class Hard(BotStgy):
    def decide_move(self,board):
        best_score=-float("inf")
        best_move=None

        for row in board.grid:
            for cell in row:
                if cell.status==CellStatus.EMPTY:
                    cell.status=CellStatus.FILLED
                    score=self.minimax(board,False)
                    cell.status=CellStatus.EMPTY

                    if score>best_score:
                        best_score=score
                        best_move=cell
        return best_move

    # -----minimax---------------------------------
    def minimax(self,board,is_maximizing):
        result=self.check_terminal(board)
        if result is not None:
            return result

        if is_maximizing:
            best_score=-float("inf")
            for row in board.grid:
                for cell in row:
                    if cell.status==CellStatus.EMPTY:
                        cell.status=CellStatus.FILLED
                        score=self.minimax(board,False)
                        cell.status=CellStatus.EMPTY
                        best_score=max(best_score,score)
            return best_score
        else:
            best_score=float("inf")
            for row in board.grid:
                for cell in row:
                    if cell.status==CellStatus.EMPTY:
                        cell.status=CellStatus.FILLED
                        score = self.minimax(board, True)
                        cell.status = CellStatus.EMPTY
                        best_score = max(best_score, score)
            return best_score

    # ---------- terminal state ------
    def check_terminnal(self,board):
        size=board.board_size

        #row
        for r in range(size):
            if all(board.grid[r][c].status==CellStatus.FILLED for c in range(size)):
                return 1

        # columns
        for c in range(size):
            if all(board.grid[r][c].status == CellStatus.FILLED for r in range(size)):
                return 1

        # diagonals
        if all(board.grid[i][i].status == CellStatus.FILLED for i in range(size)):
            return 1

        if all(board.grid[i][size - i - 1].status == CellStatus.FILLED for i in range(size)):
            return 1

        # draw
        if all(cell.status == CellStatus.FILLED for row in board.grid for cell in row):
            return 0

        return None