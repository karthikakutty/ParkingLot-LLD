
from models.CellStatus import CellStatus
from models.GameStatus import GameStatus
from helper.GameBuilder import GameBuilder
from models.GameSnapshot import GameSnapshot


class GameService:

    def start_game(self,size,players,winning_stg):
        game=GameBuilder().set_dimension(size).set_player(players).set_winning_strategies(winning_stg).build()
        return game

    def display_game(self,game):
        game.board.print_board()

    def take_move(self,game):
        game.snapshots.append(GameSnapshot(game))

        current_player=game.players[game.next_turn]
        cell=current_player.decide_cell(game.board)
        cell.player=current_player
        cell.status=CellStatus.FILLED
        game.moves.append(cell)

        if self.check_winner(game,cell):
            game.gameStatus=GameStatus.COMPLETED
            game.winner=current_player
        elif len(game.moves)==game.board.board_size * game.board.board_size:
            game.gameStatus=GameStatus.DRAW

        game.next_turn+=1
        game.next_turn %=len(game.players)


    def check_winner(self,game, cell):
        return any(ws.check_winner(cell,game.board) for ws in game.winning_strategies)

    def undo(self,game):
        if not game.moves:
            print("No moves left to undo")
            return
        cell=game.moves.pop()

        for ws in game.winning_strategies:
            ws.undo_handle(cell,game.board)

        cell.status=CellStatus.EMPTY
        cell.player=None

        game.next_turn-=1
        game.next_turn %=len(game.players)

        if not game.snapshots:
            print("No snapshot to undo")
            return
        snapshot=game.snapshots.pop()
        game.board=snapshot.board
        game.moves=snapshot.moves
        game.next_turn=snapshot.next_turn
        game.gameStatus=snapshot.gameStatus
        game.winner=snapshot.winner










