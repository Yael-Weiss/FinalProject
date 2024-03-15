from typing import Tuple
from board import Board
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
    game_settings.board.print_board(p1)
    # print(triangles_funcs.get_all_locs_4player(game_settings.board.the_board,p1))
    # print(moveValidation.get_set_of_possible_jumps(game_settings,(3,9),set({})))
    # moveValidation.move_player(game_settings,p1,)
    #functions_to_run_game.single_player_turn(game_settings,p1)
    # functions_to_run_game.play(game_settings)
    
    game_settings.board.print_board()
if __name__ == "__main__":
    main()
