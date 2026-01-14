from controller.GameController import GameController
from helper.Stratergy.diagnoalWS import DiagnoalWS
from helper.Stratergy.rowWs import RowWS
from helper.Stratergy.colWS import ColWS
from models.players import Player
from models.PlayerType import PlayerType
from models.Symbol import Symbol
from models.BotDifficulty import BotDifficulty
from services.GameServices import GameService
from models.GameStatus import GameStatus
from helper.Stratergy.winning import Winning
from models.Game import Game
from models.board import Board
from models.Bot import Bot




if __name__=='__main__':

    Gs=GameService()
    gc=GameController(Gs)

    dimensions=3

    players=[
        Player("karthika",1 , PlayerType.HUMAN,Symbol("x")),
        Bot(2,"Aarthi", Symbol("Y"),BotDifficulty.EAZY),

    ]
    winning=[RowWS(),ColWS(), DiagnoalWS()]
    game=gc.start_game(dimensions,players,winning)

    #display board
    gc.display_board(game)

    #until game in process take input
    while game.gameStatus==GameStatus.INPROGRESSED:
        current_player=game.players[game.next_turn]
        gc.take_move(game)
        gc.display_board(game)
        undo_answer=input("Undo? press 1, else continue:")
        while undo_answer=="1":
            gc.undo_move(game)
            gc.display_board(game)
            undo_answer=input("Undo again?press 1 else continue..")

    #show end game msg...
    if game.gameStatus==GameStatus.COMPLETED:
        print(f"Winner:{game.winner.name}")
    elif game.gameStatus==GameStatus.DRAW:
        print(f"Draw!")

