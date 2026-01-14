
class GameController:

    def __init__(self,gameService):
        self.gameService=gameService

    def start_game(self,size,players,winning_stg):
        return self.gameService.start_game(size,players,winning_stg)

    def display_board(self,game):
        self.gameService.display_game(game)

    def take_move(self,game):
        self.gameService.take_move(game)

    def undo_move(self,game):
        self.gameService.undo(game)



#start the game
#status game is in progress
# in LOOP
    #display the board...
    #player makes move on board
    #check for winner
    #if no winner or not all cell filled:
    #   change next_player index
    #   other player play
