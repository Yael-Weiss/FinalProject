from enum import Enum

class Triangles(Enum):
    """
    Enum class representing different types of triangles.
    
    Attributes:
        out (int): Represents a triangle that is outside the main triangle.
        upper_tri (int): Represents an upper triangle.
        upper_left_tri (int): Represents an upper left triangle.
        upper_right_tri (int): Represents an upper right triangle.
        lower_right_tri (int): Represents a lower right triangle.
        lower_tri (int): Represents a lower triangle.
        lower_left_tri (int): Represents a lower left triangle.
    """
    out=0
    upper_tri=1
    upper_left_tri=2
    upper_right_tri=3
    lower_right_tri=4
    lower_tri=5
    lower_left_tri=6