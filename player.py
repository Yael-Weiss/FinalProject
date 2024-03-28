from board_values import BoardValues
from triangles import Triangles


class Player:
    """
    Represents a player in the game.
    """

    TRIANGLES_OPPOSITES = {
        Triangles.upper_tri: Triangles.lower_tri,
        Triangles.lower_tri: Triangles.upper_tri,
        Triangles.upper_left_tri: Triangles.lower_right_tri,
        Triangles.lower_right_tri: Triangles.upper_left_tri,
        Triangles.lower_left_tri: Triangles.upper_right_tri,
        Triangles.upper_right_tri: Triangles.lower_left_tri
    }

    def __init__(self, name: str, color: BoardValues, starting_tri: Triangles, is_computer: bool = False) -> None:
        """
        Initializes a new instance of the Player class.

        Args:
            name (str): The name of the player.
            color (BoardValues): The color of the player's pieces.
            starting_tri (Triangles): The starting triangle of the player.
            is_computer (bool, optional): Indicates if the player is controlled by the computer. Defaults to False.
            destination_tri (Triangles): The triangle that the player has to move all his pieces to in order to win.
        """
        self.name = name
        self.color = color
        self.is_comp = is_computer
        self.starting_tri = starting_tri
        self.destination_tri = self.TRIANGLES_OPPOSITES[starting_tri]

    def __str__(self) -> str:
        """
        Returns a string representation of the player.

        """
        player_str = f"""{self.name}'s color: {self.color}, 
        starting triangle: {self.starting_tri}, 
        destination triangle: {self.destination_tri}\n"""
        return player_str
