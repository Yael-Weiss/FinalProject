from typing import List, Tuple
from Board import Board
from BoardValues import BoardValues
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import triangles_funcs

Coordinates = Tuple[int, int]
TRIANGLES_LIST = [Triangles.upper_tri,
                  Triangles.upper_left_tri,
                  Triangles.lower_tri,
                  Triangles.lower_right_tri,
                  Triangles.lower_left_tri,
                  Triangles.upper_right_tri]
TRIANGLES_CHECK = {Triangles.upper_tri: triangles_funcs.is_loc_in_upper_tri,
                   Triangles.upper_left_tri: triangles_funcs.is_loc_in_upper_left_tri,
                   Triangles.lower_tri: triangles_funcs.is_loc_in_lower_tri,
                   Triangles.lower_right_tri: triangles_funcs.is_loc_in_lower_right_tri,
                   Triangles.lower_left_tri: triangles_funcs.is_loc_in_lower_left_tri,
                   Triangles.upper_right_tri: triangles_funcs.is_loc_in_upper_right_tri}
DIRECTIONS_LIST=[(-2,-2),(-2,2),(2,-2),(2,2)]

# class MoveValidation:
#     def __init__(self, game_setting: GameSettings) -> None:
#         self.game_setting = game_setting

    # def get_players_destinations(self,board:Board,players_list:List[[Player]])->dict[List[[Player]],Triangles]:

def get_list_of_possible_moves(game_settings:GameSettings, location: Coordinates) -> List[Tuple[int, int]]:
    # to add jumps

    if not (game_settings.board.is_on_board(location)):
        return []

    lst = []
    row, col = location

    if (0 < row and 0 < col):
        if (game_settings.board.the_board[row-1][col-1] == BoardValues.EMPTY):
            lst.append((row-1, col-1))
    if (0 < row and col < (len(game_settings.board.the_board[0])-1)):
        if (game_settings.board.the_board[row-1][col+1] == BoardValues.EMPTY):
            lst.append((row-1, col+1))
    if (row < (len(game_settings.board.the_board)-1) and 0 < col):
        if (game_settings.board.the_board[row+1][col-1] == BoardValues.EMPTY):
            lst.append((row+1, col-1))
    if (row < (len(game_settings.board.the_board)-1) and col < (len(game_settings.board.the_board[0])-1)):
        if (game_settings.board.the_board[row+1][col+1] == BoardValues.EMPTY):
            lst.append((row+1, col+1))
    if (1 < col < (len(game_settings.board.the_board[0])-2)):
        if (game_settings.board.the_board[row][col-2] == BoardValues.EMPTY):
            lst.append((row, col-2))
        if (game_settings.board.the_board[row][col+2] == BoardValues.EMPTY):
            lst.append((row, col+2))

    return lst

def get_set_of_possible_jumps(game_settings:GameSettings, current_location:Coordinates, directions_list:List[Coordinates], possible_jumps_set: set[Coordinates]) -> set[Coordinates]:
    row, col = current_location
    for direction in directions_list:
        jump_to=(row+direction[0], col+direction[1])
        if (game_settings.board.is_on_board(jump_to)):
            # if(game_settings.board.the_board[jump_to[0]][jump_to[1]] != BoardValues.EMPTY
            #    and game_settings.board.the_board[jump_to[0]][jump_to[1]] != BoardValues.OUT_OF_BOARD):
            if (game_settings.board.the_board[jump_to[0]][jump_to[1]] == BoardValues.EMPTY and jump_to not in possible_jumps_set):
                possible_jumps_set.add(jump_to)
                get_set_of_possible_jumps(game_settings,jump_to,DIRECTIONS_LIST, possible_jumps_set)
    return possible_jumps_set

def is_in_destination(player: Player, loc: Coordinates) -> bool:
    return TRIANGLES_CHECK[player.destination_tri](loc)

def is_in_triangle_not_des(player: Player, loc: Coordinates) -> bool:
    for tri in TRIANGLES_CHECK.keys():
        if (player.destination_tri != tri):
            if (TRIANGLES_CHECK[tri](loc)):
                return True
    return False

def is_valid_move(game_settings:GameSettings,player: Player, loc: Coordinates, go_to: Coordinates) -> bool:
    if ((not is_in_triangle_not_des(player, go_to)) and player.color == game_settings.board.cell_content(loc)
            and ((go_to in get_set_of_possible_jumps(loc, set({}))) or (go_to in get_list_of_possible_moves(loc)))):
        return True
    return False

def move_player(game_settings:GameSettings,player: Player, loc: Coordinates, go_to: Coordinates) -> bool:
    if (is_valid_move(player, loc, go_to)):
        game_settings.board.the_board[loc[0]][loc[1]] = BoardValues.EMPTY
        game_settings.board.the_board[go_to[0]][go_to[1]] = player.color
        return True
    return False
