from typing import Tuple
from board import Board
from BoardValues import BoardValues
from logger import Logger
import moveValidation
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import triangles_funcs
import checking_dest
import functions_to_run_game
import prompt_toolkit
import input_provider
import read_logger

Coordinates = Tuple[int, int]
DIRECTIONS_LIST=[(-2,-2),(-2,2),(2,-2),(2,2)]




def main():
    game_settings = GameSettings()
    end_games=False
    while(not end_games):   
        game_settings=functions_to_run_game.create_game_settings(game_settings)      
        functions_to_run_game.play(game_settings)
        end_games=input_provider.make_yes_no_dialog("Chinese Checkers Game","Do you want to play again?")







    # functions_to_run_game.play()
    # board = Board()
    # game_settings = GameSettings()
    # p1=Player("y",BoardValues.RED,Triangles.upper_tri)
    # p2=Player("a",BoardValues.BLUE,Triangles.lower_tri)
    # lst=[p1,p2]
    # game_settings.board.fill_beginning_triangles(lst)
    
    # game_settings.players_list=lst
    # moveValidation.move_player(game_settings,p1,(3,15),(4,16))
    # game_settings.board.print_board()
    # moveValidation.move_player(game_settings,p1,(2,12),(4,12))
    # moveValidation.move_player(game_settings,p1,(0,12),(2,12))
    # possible_moves=moveValidation.get_all_possible_moves(game_settings,(2,12))
    # game_settings.board.print_board(p1,possible_moves)    
    # print(possible_moves)
    # print(moveValidation.is_in_triangle_not_des_not_start(p1,(4,18)))
    # print(possible_moves)
    # print(game_settings.board.print_board(p1,possible_moves))
    # print(moveValidation.move_player(game_settings,p2,(13,11),(11,9)))
    # p1.destination_tri=Triangles.upper_tri
    # game_settings.board.the_board[0][12]=BoardValues.YELLOW
    # game_settings.board.the_board[4][12]=BoardValues.RED
    # game_settings.board.print_board()
    # functions_to_run_game.play(game_settings)
    # print(moveValidation.get_set_of_possible_jumps(game_settings,(4,8),set({})))
    # print(moveValidation.get_set_of_possible_jumps(game_settings,(14,12),set({})))
    # functions_to_run_game.play(game_settings)
    # functions_to_run_game.single_player_turn(game_settings,p1)
    # # print(checking_dest.are_all_lower_tri_same_color(game_settings.board,p1))
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
    
