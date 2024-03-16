from typing import Tuple
from BoardValues import BoardValues
from board import Board
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import moveValidation

Coordinates = Tuple[int, int]


def is_p1_win_in_upper_tri(game_settings: GameSettings, p1: Player) -> bool:
    start = 12
    for i in range(1, 5):
        for j in range(i):
            if (game_settings.board.cell_content((i-1, start+2*j)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((i-1, start+2*j)) != p1.color
                    and moveValidation.get_all_possible_moves(game_settings, (i-1, start+2*j)) != []):
                return False
        start -= 1
    return True

def is_p1_win_in_upper_left_tri(game_settings:GameSettings, player: Player) -> bool:
    start_col = 0
    places_to_fill = 4
    start_row = 4
    while (start_row != 9):
        for i in range(places_to_fill):
            if(game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True

def is_p1_win_in_lower_left_tri(game_settings:GameSettings, player: Player) -> bool:
    start_col = 3
    places_to_fill = 1
    start_row = 9
    while (start_row != 13):
        for i in range(places_to_fill):
            if(game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return True

def is_p1_win_in_upper_right_tri(game_settings:GameSettings, player: Player) -> bool:
    start_col = 18
    places_to_fill = 4
    start_row = 4
    while (start_row != 9):
        for i in range(places_to_fill):
            if(game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True

def is_p1_win_in_lower_right_tri(game_settings:GameSettings, player: Player) -> bool:
    start_col = 21
    places_to_fill = 1
    start_row = 9
    while (start_row != 13):
        for i in range(places_to_fill):
            if(game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return True

def is_p1_win_in_lower_tri(game_settings:GameSettings, player: Player) -> bool:
    start_col = 9
    places_to_fill = 4
    start_row = 13
    while (start_col != 13):
        for i in range(places_to_fill):
            if(game_settings.board.cell_content((start_row, start_col+2*i)) == BoardValues.EMPTY):
                return False
            if (game_settings.board.cell_content((start_row, start_col+2*i)) != player.color
                    and moveValidation.get_all_possible_moves(game_settings, (start_row, start_col+2*i)) != []):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True

def is_p1_win_in_dest(game_settings:GameSettings, player: Player) -> bool:
    TRIANGLES_CHECK = {Triangles.upper_tri: is_p1_win_in_upper_tri,
                       Triangles.upper_left_tri: is_p1_win_in_upper_left_tri,
                       Triangles.lower_left_tri: is_p1_win_in_lower_left_tri,
                       Triangles.upper_right_tri: is_p1_win_in_upper_right_tri,
                       Triangles.lower_right_tri: is_p1_win_in_lower_right_tri,
                       Triangles.lower_tri: is_p1_win_in_lower_tri}
    return TRIANGLES_CHECK[player.destination_tri](game_settings, player)


def are_all_upper_tri_same_color(board: Board, player: Player) -> bool:
    start = 12
    for i in range(1, 5):
        for j in range(i):
            if (board.the_board[i-1][start+2*j] != player.color):
                return False
        start -= 1
    return True


def are_all_upper_left_tri_same_color(board: Board, player: Player) -> bool:
    start_col = 0
    places_to_fill = 4
    start_row = 4
    while (start_row != 9):
        for i in range(places_to_fill):
            if (board.the_board[start_row][start_col+2*i] != player.color):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True


def are_all_lower_left_tri_same_color(board: Board, player: Player) -> bool:
    start_col = 3
    places_to_fill = 1
    start_row = 9
    while (start_row != 13):
        for i in range(places_to_fill):
            if (board.the_board[start_row][start_col+2*i] != player.color):
                return False
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return True


def are_all_upper_right_tri_same_color(board: Board, player: Player) -> bool:
    start_col = 18
    places_to_fill = 4
    start_row = 4
    while (start_row != 9):
        for i in range(places_to_fill):
            if (board.the_board[start_row][start_col+2*i] != player.color):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True


def are_all_lower_right_tri_same_color(board: Board, player: Player) -> bool:
    start_col = 21
    places_to_fill = 1
    start_row = 9
    while (start_row != 13):
        for i in range(places_to_fill):
            if (board.the_board[start_row][start_col+2*i] != player.color):
                return False
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return True


def are_all_lower_tri_same_color(board: Board, player: Player) -> bool:
    start_col = 9
    places_to_fill = 4
    start_row = 13
    while (start_col != 13):
        for i in range(places_to_fill):
            if (board.the_board[start_row][start_col+2*i] != player.color):
                return False
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return True


def is_all_in_dest(board: Board, player: Player) -> bool:
    TRIANGLES_TO_DEST = {Triangles.upper_tri: are_all_upper_tri_same_color,
                         Triangles.upper_left_tri: are_all_upper_left_tri_same_color,
                         Triangles.lower_left_tri: are_all_lower_left_tri_same_color,
                         Triangles.upper_right_tri: are_all_upper_right_tri_same_color,
                         Triangles.lower_right_tri: are_all_lower_right_tri_same_color,
                         Triangles.lower_tri: are_all_lower_tri_same_color}
    return TRIANGLES_TO_DEST[player.destination_tri](board, player)
