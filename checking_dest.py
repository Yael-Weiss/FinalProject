from typing import Tuple
from board_values import BoardValues
from player import Player
from game_settings import GameSettings
from triangles import Triangles
import moveValidation

Coordinates = Tuple[int, int]


def is_p1_win_in_upper_tri(game_settings: GameSettings, p1: Player) -> bool:
    """
    Check if player 1 wins in the upper triangle.

    Args:
        game_settings (GameSettings): The settings for the game.
        p1 (Player): Player 1.

    Returns:
        bool: True if player 1 wins in the upper triangle, False otherwise.
    """
    start = game_settings.board.board_width//2
    for i in range(1, 1+game_settings.board.triangle_length):
        for j in range(i):
            if (game_settings.board.cell_content((i-1, start+2*j)) == BoardValues.EMPTY):
                return False
            if(game_settings.board.cell_content((i-1, start+2*j)) != p1.color
                    and moveValidation.get_all_possible_moves(game_settings, (i-1, start+2*j)) != []):
                return False
        start -= 1
    return True

def is_p1_win_in_upper_left_tri(game_settings: GameSettings, player: Player) -> bool:
    """
    Check if player 1 wins in the upper left triangle.

    Args:
        game_settings (GameSettings): The settings for the game.
        player (Player): Player 1.

    Returns:
        bool: True if player 1 wins in the upper left triangle, False otherwise.
    """
    start_col = 0
    places_to_fill = game_settings.board.triangle_length
    start_row = game_settings.board.triangle_length
    stop_while=(game_settings.board.triangle_length*2+1)
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True

def is_p1_win_in_lower_left_tri(game_settings: GameSettings, player: Player) -> bool:
    """
    Check if player 1 wins in the lower left triangle.

    Args:
        game_settings (GameSettings): The settings for the game.
        player (Player): Player 1.

    Returns:
        bool: True if player 1 wins in the lower left triangle, False otherwise.
    """
    start_col = game_settings.board.triangle_length-1
    places_to_fill = 1
    start_row = (game_settings.board.triangle_length*2+1)
    stop_while=start_row+game_settings.board.triangle_length
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return True

def is_p1_win_in_upper_right_tri(game_settings: GameSettings, player: Player) -> bool:
    """
    Check if player 1 wins in the upper right triangle.

    Args:
        game_settings (GameSettings): The settings for the game.
        player (Player): Player 1.

    Returns:
        bool: True if player 1 wins in the upper right triangle, False otherwise.
    """
    start_col = (game_settings.board.triangle_length*4)+2
    places_to_fill =game_settings.board.triangle_length
    start_row = game_settings.board.triangle_length
    stop_while=(game_settings.board.triangle_length*2+1)
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True

def is_p1_win_in_lower_right_tri(game_settings: GameSettings, player: Player) -> bool:
    """
    Check if player 1 wins in the lower right triangle.

    Args:
        game_settings (GameSettings): The settings for the game.
        player (Player): Player 1.

    Returns:
        bool: True if player 1 wins in the lower right triangle, False otherwise.
    """
    start_col = ((game_settings.board.triangle_length*4)+2+(game_settings.board.triangle_length-1))
    places_to_fill = 1
    start_row = game_settings.board.triangle_length*2+1
    stop_while=start_row+game_settings.board.triangle_length
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return True

def is_p1_win_in_lower_tri(game_settings: GameSettings, player: Player) -> bool:
    """
    Check if player 1 wins in the lower triangle.

    Args:
        game_settings (GameSettings): The settings for the game.
        player (Player): Player 1.

    Returns:
        bool: True if player 1 wins in the lower triangle, False otherwise.
    """
    start_col = game_settings.board.triangle_length*2+1
    places_to_fill = game_settings.board.triangle_length
    start_row = game_settings.board.board_length-game_settings.board.triangle_length
    stop_while = (start_col+game_settings.board.triangle_length)
    while (start_col != stop_while):
        for i in range(places_to_fill):
            if (game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True

def is_p1_win_in_dest(game_settings: GameSettings, player: Player) -> bool:
    """
    Check if player 1 wins in their destination triangle.

    Args:
        game_settings (GameSettings): The settings for the game.
        player (Player): Player 1.

    Returns:
        bool: True if player 1 wins in their destination triangle, False otherwise.
    """
    TRIANGLES_CHECK = {Triangles.upper_tri: is_p1_win_in_upper_tri,
                       Triangles.upper_left_tri: is_p1_win_in_upper_left_tri,
                       Triangles.lower_left_tri: is_p1_win_in_lower_left_tri,
                       Triangles.upper_right_tri: is_p1_win_in_upper_right_tri,
                       Triangles.lower_right_tri: is_p1_win_in_lower_right_tri,
                       Triangles.lower_tri: is_p1_win_in_lower_tri}
    return TRIANGLES_CHECK[player.destination_tri](game_settings, player)
