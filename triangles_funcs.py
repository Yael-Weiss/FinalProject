
from typing import List, Tuple

from Board import Board
from player import Player
from triangles import Triangles


Coordinates = Tuple[int, int]
EMOJI_LIST=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
# NUM_ROWS_IN_TRIANGLE = 4
# MIDDLE_OF_ROW = 12


def is_loc_in_upper_tri(loc: Coordinates) -> bool:
    # if (loc[0] in range(NUM_ROWS_IN_TRIANGLE) and loc[1] in range(MIDDLE_OF_ROW - loc[0], MIDDLE_OF_ROW + 2*loc[0], 2)):
    #     return True

    # return False
    start=12
    for i in range(1, 5):
        for j in range(i):
            if ((i-1) == loc[0] and (start+2*j) == loc[1]):
                return True
        start -= 1
    return False

def is_loc_in_upper_left_tri(loc: Coordinates) -> bool:
    start_col = 0
    places_to_fill = 4
    start_row = 4
    while (start_row != 9):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return False

def is_loc_in_lower_left_tri(loc: Coordinates) -> bool:
    start_col = 3
    places_to_fill = 1
    start_row = 9
    while (start_row != 13):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return False

def is_loc_in_upper_right_tri(loc: Coordinates) -> bool:
    start_col = 18
    places_to_fill = 4
    start_row = 4
    while (start_row != 9):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return False

def is_loc_in_lower_right_tri(loc: Coordinates) -> bool:
    start_col = 21
    places_to_fill = 1
    start_row = 9
    while (start_row != 13):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return False

def is_loc_in_lower_tri(loc: Coordinates) -> bool:
    start_col = 9
    places_to_fill = 4
    start_row = 13
    while (start_col != 13):
        for i in range(places_to_fill):
            if (start_row == loc[0] and (start_col+2*i) == loc[1]):
                return True
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return False


def get_list_of_locs_in_upper_tri(board:Board) -> List[Coordinates]:
    # if (loc[0] in range(NUM_ROWS_IN_TRIANGLE) and loc[1] in range(MIDDLE_OF_ROW - loc[0], MIDDLE_OF_ROW + 2*loc[0], 2)):
    #     return True

    # return False
    start=12
    lst=[]
    for i in range(1, 5):
        for j in range(i):
            lst.append((i-1,start+2*j))
        start -= 1
    return lst

def get_list_of_locs_in_upper_left_tri(board:Board) -> List[Coordinates]:
    start_col = 0
    places_to_fill = 4
    start_row = 4
    lst=[]
    while (start_row != 9):
        for i in range(places_to_fill):
            lst.append((start_row,start_col+2*i))
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return lst

def get_list_of_locs_in_lower_left_tri(board:Board) -> List[Coordinates]:
    start_col = 3
    places_to_fill = 1
    start_row = 9
    lst=[]
    while (start_row != 13):
        for i in range(places_to_fill):
            lst.append((start_row,start_col+2*i))
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return lst

def get_list_of_locs_in_upper_right_tri(board:Board) -> List[Coordinates]:
    start_col = 18
    places_to_fill = 4
    start_row = 4
    lst=[]
    while (start_row != 9):
        for i in range(places_to_fill):
            lst.append((start_row,start_col+2*i))
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return lst

def get_list_of_locs_in_lower_right_tri(board:Board) -> List[Coordinates]:
    start_col = 21
    places_to_fill = 1
    start_row = 9
    lst=[]
    while (start_row != 13):
        for i in range(places_to_fill):
            lst.append((start_row,start_col+2*i))
        start_col -= 1
        start_row += 1
        places_to_fill += 1
    return lst

def get_list_of_locs_in_lower_tri(board:Board) -> List[Coordinates]:
    start_col = 9
    places_to_fill = 4
    start_row = 13
    lst=[]
    while (start_col != 13):
        for i in range(places_to_fill):
            lst.append((start_row,start_col+2*i))
            index+=1
        start_col += 1
        start_row += 1
        places_to_fill -= 1
    return lst
if __name__ == "__main__":
    pass
