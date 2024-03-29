import copy
from typing import List, Tuple
from board_values import BoardValues
from player import Player
from game_settings import GameSettings
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
DIRECTIONS_LIST = [(-2, -2), (-2, 2), (2, -2), (2, 2), (2, 0), (-2, 0),(0, 2), (0, -2)]


def get_list_of_possible_moves(game_settings: GameSettings, current_loc: Coordinates) -> List[Tuple[int, int]]:
    """
    Returns a list of possible moves from the current location on the game board.

    Args:
        game_settings (GameSettings): The settings of the game.
        current_loc (Coordinates): The current location on the game board.

    Returns:
        List[Tuple[int, int]]: A list of tuples representing the possible moves.
                               Each tuple contains the row and column of a valid move.
    """
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
    if (-1 < col < (len(game_settings.board.the_board[0])-2)):
        if (game_settings.board.the_board[row][col+2] == BoardValues.EMPTY):
            lst.append((row, col+2))
    if (1 < row < (len(game_settings.board.the_board)-2)):
        if (game_settings.board.the_board[row-2][col] == BoardValues.EMPTY):
            lst.append((row-2, col))
    if (-1 < row < (len(game_settings.board.the_board)-2)):
        if (game_settings.board.the_board[row+2][col] == BoardValues.EMPTY):
            lst.append((row+2, col))

    return lst

def get_set_of_possible_jumps(game_settings: GameSettings, current_location: Coordinates, possible_jumps_set: set[Coordinates], directions_list: List[Coordinates] = DIRECTIONS_LIST) -> set[Coordinates]:
    """
    Returns a set of possible jump locations from the current location on the game board.

    Args:
        game_settings (GameSettings): The settings of the game.
        current_location (Coordinates): The current location on the game board.
        possible_jumps_set (set[Coordinates]): in the first call for the function it has to be an empty set.
        directions_list (List[Coordinates], optional): The list of directions to check for possible jumps. Defaults to DIRECTIONS_LIST.

    Returns:
        set[Coordinates]: The set of possible jump locations.
    """
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
    """
    Finds the player object associated with the color of the cell at the current location.

    Args:
        game_settings (GameSettings): The settings of the game.
        current_loc (Coordinates): The current location to check.

    Returns:
        Player: The player object associated with the color of the cell at the current location, or None if no player is found.
    """
    for player in game_settings.players_list:
        if game_settings.board.cell_content(current_loc) == player.color:
            return player
    return None

def get_all_possible_moves(game_settings: GameSettings, current_loc: Coordinates) -> List[Tuple[int, int]]:
    """
    Get all possible moves for a given game state and current location.

    Args:
        game_settings (GameSettings): The settings of the game.
        current_loc (Coordinates): The current location on the game board.

    Returns:
        List[Tuple[int, int]]: A list of tuples representing the possible moves and jumps.
    """
    possible_moves = get_list_of_possible_moves(game_settings, current_loc)
    possible_jumps = list(get_set_of_possible_jumps(
        game_settings, current_loc, set({})))
    possible_moves.extend(list(possible_jumps))
    player = from_current_loc_to_player(game_settings, current_loc)
    copy_possible_moves = copy.copy(possible_moves)
    for move_loc in copy_possible_moves:
        if (is_in_triangle_not_des_not_start(game_settings, player, move_loc)):
            possible_moves.remove(move_loc)
    return possible_moves

def is_in_triangle_not_des_not_start(game_settings: GameSettings, player: Player, loc: Coordinates) -> bool:
    """
    Checks if the given location is in a triangle that is neither the destination triangle nor the starting triangle of the player.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player for whom the validation is being performed.
        loc (Coordinates): The location to be checked.

    Returns:
        bool: True if the location is in a triangle that is neither the destination triangle nor the starting triangle of the player, False otherwise.
    """
    for tri in TRIANGLES_CHECK.keys():
        if (player.destination_tri != tri and player.starting_tri != tri):
            if (TRIANGLES_CHECK[tri](game_settings.board, loc)):
                return True
    return False

def is_valid_current_loc(game_settings: GameSettings, player: Player, current_loc: Coordinates) -> bool:
    """
    Check if the current location is valid for the player in the given game settings.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player whose current location is being checked.
        current_loc (Coordinates): The current location to be checked.

    Returns:
        bool: True if the current location is valid for the player, False otherwise.
    """
    return game_settings.board.cell_content(current_loc) == player.color and get_all_possible_moves(game_settings, current_loc) != []

def is_valid_move(game_settings: GameSettings, player: Player, current_loc: Coordinates, go_to: Coordinates) -> bool:
    """
    Checks if a move is valid for a given player in a game.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player making the move.
        loc (Coordinates): The current location of the player.
        go_to (Coordinates): The location the player wants to move to.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    if (not is_in_triangle_not_des_not_start(game_settings, player, go_to)) and player.color == game_settings.board.cell_content(current_loc) and (go_to in get_all_possible_moves(game_settings, current_loc)):
        return True
    return False

def move_player(game_settings: GameSettings, player: Player, loc: Coordinates, go_to: Coordinates) -> bool:
    """
    Moves the player on the game board from the current location to the specified location.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player object representing the player.
        loc (Coordinates): The current location of the player.
        go_to (Coordinates): The location to move the player to.

    Returns:
        bool: True if the move is valid and successful, False otherwise.
    """
    if (is_valid_move(game_settings, player, loc, go_to)):
        game_settings.board.the_board[loc[0]][loc[1]] = BoardValues.EMPTY
        game_settings.board.the_board[go_to[0]][go_to[1]] = player.color
        return True
    return False
