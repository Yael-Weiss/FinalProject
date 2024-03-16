from typing import Tuple
from board import Board
from player import Player
from triangles import Triangles

Coordinates = Tuple[int, int]


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
