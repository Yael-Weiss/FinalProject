
from typing import List, Tuple


from BoardValues import BoardValues
from player import Player



Coordinates = Tuple[int, int]

# NUM_ROWS_IN_TRIANGLE = 4
# MIDDLE_12OF_ROW = 

def get_all_locs_4player(board:List[List[BoardValues]],player:Player)->List[Coordinates]:
    lst=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==player.color):
                lst.append((i,j))
    return lst













# def get_list_of_locs_in_upper_tri(board:Board) -> List[Coordinates]:
#     # if (loc[0] in range(NUM_ROWS_IN_TRIANGLE) and loc[1] in range(MIDDLE_OF_ROW - loc[0], MIDDLE_OF_ROW + 2*loc[0], 2)):
#     #     return True

#     # return False
#     start=12
#     lst=[]
#     for i in range(1, 5):
#         for j in range(i):
#             lst.append((i-1,start+2*j))
#         start -= 1
#     return lst

# def get_list_of_locs_in_upper_left_tri(board:Board) -> List[Coordinates]:
#     start_col = 0
#     places_to_fill = 4
#     start_row = 4
#     lst=[]
#     while (start_row != 9):
#         for i in range(places_to_fill):
#             lst.append((start_row,start_col+2*i))
#         start_col += 1
#         start_row += 1
#         places_to_fill -= 1
#     return lst

# def get_list_of_locs_in_lower_left_tri(board:Board) -> List[Coordinates]:
#     start_col = 3
#     places_to_fill = 1
#     start_row = 9
#     lst=[]
#     while (start_row != 13):
#         for i in range(places_to_fill):
#             lst.append((start_row,start_col+2*i))
#         start_col -= 1
#         start_row += 1
#         places_to_fill += 1
#     return lst

# def get_list_of_locs_in_upper_right_tri(board:Board) -> List[Coordinates]:
#     start_col = 18
#     places_to_fill = 4
#     start_row = 4
#     lst=[]
#     while (start_row != 9):
#         for i in range(places_to_fill):
#             lst.append((start_row,start_col+2*i))
#         start_col += 1
#         start_row += 1
#         places_to_fill -= 1
#     return lst

# def get_list_of_locs_in_lower_right_tri(board:Board) -> List[Coordinates]:
#     start_col = 21
#     places_to_fill = 1
#     start_row = 9
#     lst=[]
#     while (start_row != 13):
#         for i in range(places_to_fill):
#             lst.append((start_row,start_col+2*i))
#         start_col -= 1
#         start_row += 1
#         places_to_fill += 1
#     return lst

# def get_list_of_locs_in_lower_tri(board:Board) -> List[Coordinates]:
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
