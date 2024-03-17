from BoardValues import BoardValues
from triangles import Triangles


class Player:
    """

    """
    TRIANGLES_OPPOSITES = {Triangles.upper_tri: Triangles.lower_tri,
                           Triangles.lower_tri: Triangles.upper_tri,
                           Triangles.upper_left_tri: Triangles.lower_right_tri,
                           Triangles.lower_right_tri: Triangles.upper_left_tri,
                           Triangles.lower_left_tri: Triangles.upper_right_tri,
                           Triangles.upper_right_tri: Triangles.lower_left_tri
                           }

    def __init__(self, name: str, color: BoardValues, starting_tri: Triangles,is_computer:bool=False) -> None:
        self.name = name
        self.color = color
        self.is_comp = is_computer
        self.starting_tri = starting_tri
        self.destination_tri = self.TRIANGLES_OPPOSITES[starting_tri]

    def __str__(self) -> str:
        player_str = f"{self.name}'s color: {self.color}, starting triangle: {self.starting_tri}, destination triangle:{self.destination_tri}\n"
        return player_str
