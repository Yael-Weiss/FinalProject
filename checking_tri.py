
from typing import Tuple
from board import Board


Coordinates = Tuple[int, int]

def is_loc_in_upper_tri(board:Board,loc: Coordinates) -> bool:
    # if (loc[0] in range(NUM_ROWS_IN_TRIANGLE) and loc[1] in range(MIDDLE_OF_ROW - loc[0], MIDDLE_OF_ROW + 2*loc[0], 2)):
    #     return True

    # return False
    start=board.board_width//2
    for i in range(1, board.triangle_length+1):
        for j in range(i):
            if ((i-1) == loc[0] and (start+2*j) == loc[1]):
                return True
        start -= 1
    return False

def is_loc_in_upper_left_tri(board:Board,loc: Coordinates) -> bool:
    start_col = 0
    places_to_fill = board.triangle_length
    start_row = board.triangle_length
    stop_while=(board.triangle_length*2+1)
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return False

def is_loc_in_lower_left_tri(board:Board,loc: Coordinates) -> bool:
    start_col = board.triangle_length-1
    places_to_fill = 1
    start_row = (board.triangle_length*2+1)
    stop_while=start_row+board.triangle_length
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return False

def is_loc_in_upper_right_tri(board:Board,loc: Coordinates) -> bool:
    start_col = (board.triangle_length*4)+2
    places_to_fill = board.triangle_length
    start_row = board.triangle_length
    stop_while=(board.triangle_length*2+1)
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return False

def is_loc_in_lower_right_tri(board:Board,loc: Coordinates) -> bool:
    start_col = ((board.triangle_length*4)+2+(board.triangle_length-1))
    places_to_fill = 1
    start_row = (board.triangle_length*2+1)
    stop_while=start_row+board.triangle_length
    while (start_row != stop_while):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return False

def is_loc_in_lower_tri(board:Board,loc: Coordinates) -> bool:
    start_col = (2*board.triangle_length)+1
    places_to_fill = board.triangle_length
    start_row = board.board_length-board.triangle_length
    stop_while = (start_col+board.triangle_length)
    while (start_col != stop_while):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return False

