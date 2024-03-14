from typing import Tuple
from Board import Board
from BoardValues import BoardValues
import moveValidation
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import triangles_funcs
import checking_dest

Coordinates = Tuple[int, int]
DIRECTIONS_LIST=[(-2,-2),(-2,2),(2,-2),(2,2),(0,2),(0,-2)]

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
    # move = MoveValidation(game_settings)
    # # print((4,8) in move.get_list_of_possible_moves((3,9)))
    # # print(move.is_in_triangle_not_des(p1,(4,8)))
    # move.move_player(p1,(3,9),(4,8))
    # game_settings.board.print_board()
    # print(checking_dest.is_all_in_upper_tri_same_color(game_settings.board,p1))
    # print(p1.color)
    # print(move.game_setting.board.cell_content((3,9)))
    print(moveValidation.get_set_of_possible_jumps(game_settings,(9,11),DIRECTIONS_LIST,set({})))

if __name__ == "__main__":
    main()
