
class Player:
    def __init__(self,name,id,type,symbol):
        self.name=name
        self.id=id
        self.type=type
        self.symbol=symbol


    def decide_cell(self,board):
        while True:
            row=int(input("Enter row:"))-1
            col=int(input("Enter column: "))-1
            if 0<=row<board.board_size and 0 <=col<board.board_size:
                if board.grid[row][col].status=="EMPTY":
                    return board.grid[row][col]

                print("Invalid row or column or cell is filled")
