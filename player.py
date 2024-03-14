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

    def __init__(self, name: str, color: BoardValues, starting_tri: Triangles) -> None:
        self.name = name
        self.color = color
        self.starting_tri = starting_tri
        self.destination_tri = self.TRIANGLES_OPPOSITES[starting_tri]

    def __str__(self) -> str:
        player_str = f"{self.name}'s color: {self.color}"
        return player_str
