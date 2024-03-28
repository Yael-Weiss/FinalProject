from typing import List, Tuple
from BoardValues import BoardValues
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import checking_tri

Coordinates = Tuple[int, int]
TRIANGLES_LIST = [Triangles.upper_tri,
                  Triangles.upper_left_tri,
                  Triangles.lower_tri,
                  Triangles.lower_right_tri,
                  Triangles.lower_left_tri,
                  Triangles.upper_right_tri]
TRIANGLES_CHECK = {Triangles.upper_tri: checking_tri.is_loc_in_upper_tri,
                   Triangles.upper_left_tri: checking_tri.is_loc_in_upper_left_tri,
                   Triangles.lower_tri: checking_tri.is_loc_in_lower_tri,
                   Triangles.lower_right_tri: checking_tri.is_loc_in_lower_right_tri,
                   Triangles.lower_left_tri: checking_tri.is_loc_in_lower_left_tri,
                   Triangles.upper_right_tri: checking_tri.is_loc_in_upper_right_tri}
DIRECTIONS_LIST = [(-2, -2), (-2, 2), (2, -2), (2, 2), (2, 0), (-2, 0)]

def get_list_of_possible_moves(game_settings: GameSettings, current_loc: Coordinates) -> List[Tuple[int, int]]:
    if not (game_settings.board.is_on_board(current_loc)):
        return []

    lst = []
    row, col = current_loc

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
    if (1 < row < (len(game_settings.board.the_board)-2)):
        if (game_settings.board.the_board[row-2][col] == BoardValues.EMPTY):
            lst.append((row-2, col))
        if (game_settings.board.the_board[row+2][col] == BoardValues.EMPTY):
            lst.append((row+2, col))

    return lst

def get_set_of_possible_jumps(game_settings: GameSettings, current_location: Coordinates, possible_jumps_set: set[Coordinates], directions_list: List[Coordinates] = DIRECTIONS_LIST) -> set[Coordinates]:
    row, col = current_location
    for direction in directions_list:
        jump_to = (row+direction[0], col+direction[1])
        if (game_settings.board.is_on_board(jump_to)):
            if (game_settings.board.the_board[(row+jump_to[0])//2][(col+jump_to[1])//2] != BoardValues.EMPTY
               and game_settings.board.the_board[(row+jump_to[0])//2][(col+jump_to[1])//2] != BoardValues.OUT_OF_BOARD):
                if (game_settings.board.the_board[jump_to[0]][jump_to[1]] == BoardValues.EMPTY and jump_to not in possible_jumps_set):
                    possible_jumps_set.add(jump_to)
                    get_set_of_possible_jumps(
                        game_settings, jump_to, possible_jumps_set)
    return possible_jumps_set

def from_current_loc_to_player(game_settings: GameSettings, current_loc: Coordinates) -> Player:
    for player in game_settings.players_list:
        if (game_settings.board.cell_content(current_loc) == player.color):
            return player
    return None

def get_all_possible_moves(game_settings: GameSettings, current_loc: Coordinates) -> List[Tuple[int, int]]:
    possible_moves = get_list_of_possible_moves(game_settings, current_loc)
    possible_jumps = list(get_set_of_possible_jumps(
        game_settings, current_loc, set({})))
    possible_moves.extend(list(possible_jumps))
    player = from_current_loc_to_player(game_settings, current_loc)
    for move in possible_moves:
        if (is_in_triangle_not_des_not_start(game_settings,player, move)):
            possible_moves.remove(move)
    return possible_moves

def is_in_triangle_not_des_not_start(game_settings:GameSettings,player: Player, loc: Coordinates) -> bool:
    for tri in TRIANGLES_CHECK.keys():
        if (player.destination_tri != tri and player.starting_tri != tri):
            if (TRIANGLES_CHECK[tri](game_settings.board,loc)):
                return True
    return False

def is_valid_current_loc(game_settings: GameSettings, player: Player, current_loc: Coordinates) -> bool:
    return game_settings.board.cell_content(current_loc) == player.color and get_all_possible_moves(game_settings, current_loc) != []

def is_valid_move(game_settings: GameSettings, player: Player, loc: Coordinates, go_to: Coordinates) -> bool:
    if (not is_in_triangle_not_des_not_start(game_settings,player, go_to)) and player.color == game_settings.board.cell_content(loc) and (go_to in get_all_possible_moves(game_settings, loc)):
        return True
    return False

def move_player(game_settings: GameSettings, player: Player, loc: Coordinates, go_to: Coordinates) -> bool:
    if (is_valid_move(game_settings, player, loc, go_to)):
        game_settings.board.the_board[loc[0]][loc[1]] = BoardValues.EMPTY
        game_settings.board.the_board[go_to[0]][go_to[1]] = player.color
        return True
    return False


if __name__ == "__main__":
    pass
    
