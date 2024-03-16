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
import prompt_toolkit

Coordinates = Tuple[int, int]
DIRECTIONS_LIST=[(-2,-2),(-2,2),(2,-2),(2,2)]

def main():
    functions_to_run_game.play()
    # print("Welcome to Chinese Checkers Game!")
    # board = Board()
    # game_settings = GameSettings()
    # # game_settings.init_board()
    # p1=Player("y",BoardValues.RED,Triangles.upper_tri)
    # p2=Player("a",BoardValues.BLUE,Triangles.lower_tri)
    # lst=[p1,p2]
    # game_settings.board.fill_beginning_triangles(lst)
    # game_settings.players_list=lst
    # print(moveValidation.move_player(game_settings,p1,(3,9),(4,8)))
    # # game_settings.board.print_board()
    # print(checking_dest.are_all_lower_tri_same_color(game_settings.board,p1))
    # print(p1.destination_tri)
    # print(checking_dest.is_all_in_dest(game_settings.board,p1))
    # # functions_to_run_game.single_round(game_settings)   
    
    
    # print(moveValidation.get_set_of_possible_jumps(game_settings,(3,9),set({})))
    # game_settings.board.print_board(p1)
    # piece_to_move=functions_to_run_game.player_choose_piece_to_move(game_settings,p1)
    # print(piece_to_move)
    # # game_settings.board.clear_screen()
    # moves=list(moveValidation.get_all_possible_moves(game_settings,piece_to_move))
    # print(moves)
    # game_settings.board.print_board(p1,moves)
    # go_to=functions_to_run_game.player_choose_destination(game_settings,p1,piece_to_move)
    # print(go_to)
    # # # print(functions_to_run_game.player_choose_piece_to_move(game_settings,p1))
    
    
    # print(triangles_funcs.get_all_locs_4player(game_settings.board.the_board,p1))
    # moveValidation.move_player(game_settings,p1,)
    #functions_to_run_game.single_player_turn(game_settings,p1)
    # functions_to_run_game.play(game_settings)
    
    # game_settings.board.print_board(None,moves)
if __name__ == "__main__":
    main()
