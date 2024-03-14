
from typing import Tuple


Coordinates = Tuple[int, int]
def is_loc_in_upper_tri(loc: Coordinates) -> bool:
        start = 12
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

if __name__=="__main__":
    pass