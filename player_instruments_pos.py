
from typing import List, Tuple
from board_values import BoardValues
from player import Player

Coordinates = Tuple[int, int]

def get_all_locs_4player(board:List[List[BoardValues]],player:Player)->List[Coordinates]:
    lst=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==player.color):
                lst.append((i,j))
    return lst
