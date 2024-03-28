from enum import Enum
from enum import Enum

class BoardValues(Enum):
    """
    Enum class representing the values of the game board.

    Attributes:
        EMPTY (int): Represents an empty cell on the board.
        OUT_OF_BOARD (int): Represents a cell that is out of the board.
        RED (int): Represents a cell with the color red.
        BLUE (int): Represents a cell with the color blue.
        YELLOW (int): Represents a cell with the color yellow.
        PURPLE (int): Represents a cell with the color purple.
        GREEN (int): Represents a cell with the color green.
        ORANGE (int): Represents a cell with the color orange.
    """
    EMPTY=-1
    OUT_OF_BOARD=0
    RED=1
    BLUE=2
    YELLOW=3
    PURPLE=4
    GREEN=5
    ORANGE=6
    