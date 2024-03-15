from typing import Tuple
from Board import Board
from BoardValues import BoardValues
import moveValidation
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import triangles_funcs
import checking_dest
import functions_to_run_game

Coordinates = Tuple[int, int]
DIRECTIONS_LIST=[(-2,-2),(-2,2),(2,-2),(2,2)]

def main():
    print("Welcome to Chinese Checkers Game!")
    board = Board()
    game_settings = GameSettings()
    # game_settings.init_board()
    p1=Player("y",BoardValues.RED,Triangles.upper_tri)
    p2=Player("a",BoardValues.BLUE,Triangles.lower_tri)
    lst=[p1,p2]
    game_settings.board.fill_beginning_triangles(lst)
    game_settings.board.print_board()
    functions_to_run_game.single_player_turn(game_settings,p1)
    # functions_to_run_game.play(game_settings)
if __name__ == "__main__":
    main()
