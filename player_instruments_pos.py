
from typing import List, Tuple
from board_values import BoardValues
from player import Player

Coordinates = Tuple[int, int]

from typing import List, Tuple

def get_all_locs_4player(board:List[List[BoardValues]],player:Player)->List[Coordinates]:
    """
    Returns a list of coordinates representing the locations of the pieces of a specific player on the board.

    Args:
        board (List[List[BoardValues]]): A 2D list representing the game board.
        player (Player): The player whose locations need to be found.

    Returns:
        List[Tuple[int, int]]: A list of coordinates (tuples) representing the locations of the pieces of the player on the board.
    """
    lst=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==player.color):
                lst.append((i,j))
    return lst
