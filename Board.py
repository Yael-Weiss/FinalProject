from typing import List, Tuple
from typing import Tuple, List
from board_values import BoardValues
from player import Player
from triangles import Triangles
import player_instruments_pos


Coordinates = Tuple[int, int]
EMOJY_DICT = {
    BoardValues.EMPTY: "⚪",
    BoardValues.OUT_OF_BOARD: "  ",
    BoardValues.RED: "🔴",
    BoardValues.BLUE: "🔵",
    BoardValues.YELLOW: "🟡",
    BoardValues.PURPLE: "🟣",
    BoardValues.GREEN: "🟢",
    BoardValues.ORANGE: "🟠"
}
START_EMOJI = "🐫"
# EMOJI_POSSIBLE_MOVES = [i for i in range()]
# ["😽" ,"🐶","🦊","🐒", "🐺" ,"🐱","🐷","🐮", "🦝","🐯","🐗",
#                         "🐭" ,"🐹","🐰","🐻", "🫎" ,"🐨","🐼","🐸", "🦧" ,"🐔","🐕","🐩",
#                         "🦛" ,"🦥","🦖","🐬", "🦭" ,"🐓","💩","🐖", "🦐" ,"🦑","🦆","🦀","🦞"]


class Board:
    """
    Represents a game board.

    Args:
        triangle_length (int): The length of each triangle in the board. Default is 4.

    Attributes:
        triangle_length (int): The length of each triangle in the board.
        pieces_nums (List[str]): A list of strings representing the numbers of the pieces on the board.
        board_length (int): The length of the board.
        board_width (int): The width of the board.
        the_board (List[List[BoardValues]]): The 2D list representing the board.

    """

    def __init__(self, triangle_length: int = 4) -> None:
        self.triangle_length = triangle_length
        self.pieces_nums = self.get_pieces_nums(self.triangle_length)
        self.board_length = self.triangle_length * 4 + 1
        self.board_width = self.triangle_length * 6 + 1
        self.the_board = self.get_empty_board()

    def get_empty_board(self) -> List[List[BoardValues]]:
        """
        Returns an empty board with the specified dimensions.

        Returns:
            List[List[BoardValues]]: The empty board.

        """
        lst = []
        temp_lst = []
        empty_places = 1
        out_of_board = self.board_width//2
        while (empty_places != self.triangle_length+1):
            for i in range(out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)
            for j in range(empty_places):
                if (j == empty_places-1):
                    temp_lst.append(BoardValues.EMPTY)
                else:
                    temp_lst.append(BoardValues.EMPTY)
                    temp_lst.append(BoardValues.OUT_OF_BOARD)
            for i in range(out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)
            out_of_board -= 1
            empty_places += 1
            lst.append(temp_lst)
            temp_lst = []

        empty_places = self.board_width//2+1
        out_of_board = 0
        while (out_of_board != self.triangle_length+1):

            for i in range(0, out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)

            for j in range(empty_places):
                if (j == empty_places-1):
                    temp_lst.append(BoardValues.EMPTY)
                else:
                    temp_lst.append(BoardValues.EMPTY)
                    temp_lst.append(BoardValues.OUT_OF_BOARD)

            for k in range(out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)
            empty_places -= 1
            out_of_board += 1
            lst.append(temp_lst)
            temp_lst = []

        empty_places = self.triangle_length*2+2
        out_of_board = self.triangle_length-1
        while (out_of_board != -1):
            for i in range(out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)
            for j in range(empty_places):
                if (j == empty_places-1):
                    temp_lst.append(BoardValues.EMPTY)
                else:
                    temp_lst.append(BoardValues.EMPTY)
                    temp_lst.append(BoardValues.OUT_OF_BOARD)
            for k in range(out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)
            out_of_board -= 1
            empty_places += 1
            lst.append(temp_lst)
            temp_lst = []

        empty_places = self.triangle_length
        out_of_board = (self.triangle_length*2)+1
        while (empty_places != 0):
            for i in range(out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)
            for j in range(empty_places):
                if (j == empty_places-1):
                    temp_lst.append(BoardValues.EMPTY)
                else:
                    temp_lst.append(BoardValues.EMPTY)
                    temp_lst.append(BoardValues.OUT_OF_BOARD)
            for i in range(out_of_board):
                temp_lst.append(BoardValues.OUT_OF_BOARD)
            out_of_board += 1
            empty_places -= 1
            lst.append(temp_lst)
            temp_lst = []
        return lst

    def fill_upper_triangle(self, player_color: BoardValues) -> None:
        """
        Fills the upper triangle of the board with the specified player's color.

        Args:
            player_color (BoardValues): The color of the player.

        Returns:
            None

        """
        start = self.board_width//2
        for i in range(1, 1+self.triangle_length):
            for j in range(i):
                self.the_board[i-1][start+2*j] = player_color
            start -= 1

    def fill_lower_triangle(self, player_color: BoardValues) -> None:
        """
        Fills the lower triangle of the board with the specified player's color.

        Args:
            player_color (BoardValues): The color of the player.

        Returns:
            None

        """
        start_col = (2*self.triangle_length)+1
        places_to_fill = self.triangle_length
        start_row = self.board_length-self.triangle_length
        stop_while = (start_col+self.triangle_length)
        while (start_col != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1

    def fill_upper_left_triangle(self, player_color: BoardValues) -> None:
        """
        Fills the upper left triangle of the board with the specified player's color.

        Args:
            player_color (BoardValues): The color of the player.

        Returns:
            None

        """
        start_col = 0
        places_to_fill = self.triangle_length
        start_row = self.triangle_length
        stop_while = ((start_row+self.triangle_length)+1)
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1

    def fill_lower_left_triangle(self, player_color: BoardValues) -> None:
        """
        Fills the lower left triangle of the board with the specified player's color.

        Args:
            player_color (BoardValues): The color of the player.

        Returns:
            None

        """
        start_col = self.triangle_length-1
        places_to_fill = 1
        start_row = (self.triangle_length*2+1)
        stop_while = start_row+self.triangle_length
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col -= 1
            start_row += 1
            places_to_fill += 1

    def fill_upper_right_triangle(self, player_color: BoardValues) -> None:
        """
        Fills the upper right triangle of the board with the specified player's color.

        Args:
            player_color (BoardValues): The color of the player.

        Returns:
            None

        """
        start_col = (self.triangle_length*4)+2
        places_to_fill = self.triangle_length
        start_row = self.triangle_length
        stop_while = (self.triangle_length*2+1)
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1

    def fill_lower_right_triangle(self, player_color: BoardValues) -> None:
        """
        Fills the lower right triangle of the board with the specified player's color.

        Args:
            player_color (BoardValues): The color of the player.

        Returns:
            None

        """
        start_col = ((self.triangle_length*4)+2+(self.triangle_length-1))
        places_to_fill = 1
        start_row = (self.triangle_length*2+1)
        stop_while = start_row+self.triangle_length
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col -= 1
            start_row += 1
            places_to_fill += 1

    def fill_beginning_triangles(self, players_list: List[Player]) -> None:
        """
        Fills the beginning triangles on the board for each player.

        Args:
            players_list (List[Player]): A list of Player objects representing the players in the game.

        Returns:
            None
        """
        for player in players_list:
            if player.starting_tri == Triangles.upper_tri:
                self.fill_upper_triangle(player.color)
            if player.starting_tri == Triangles.upper_left_tri:
                self.fill_upper_left_triangle(player.color)
            if player.starting_tri == Triangles.upper_right_tri:
                self.fill_upper_right_triangle(player.color)
            if player.starting_tri == Triangles.lower_right_tri:
                self.fill_lower_right_triangle(player.color)
            if player.starting_tri == Triangles.lower_tri:
                self.fill_lower_triangle(player.color)
            if player.starting_tri == Triangles.lower_left_tri:
                self.fill_lower_left_triangle(player.color)

    def set_triangle_length(self, tri_length: int):
        """
        Set the length of the triangle.

        Args:
            tri_length (int): The length of the triangle.

        Returns:
            None
        """
        self.triangle_length = tri_length

    def match_cell_to_emojy(self, player_color: BoardValues):
        """
        Matches the player's color to an emoji color representation.

        Args:
            player_color (BoardValues): The color of the player.

        Returns:
            str: The emoji representation of the player's color.
        """
        return EMOJY_DICT[player_color]

    def clear_screen(self) -> None:
        """
        Clears the terminal screen.

        This method clears the terminal screen by printing the escape sequence
        '\033[H\033[J', which moves the cursor to the top-left corner of the
        screen and clears the entire screen.

        Args:
            self: The Board object.

        Returns:
            None
        """
        print("\033[H\033[J", end="")

    def print_board(self, player: Player = None, possible_moves: List[Tuple[int, int]] = None, current_loc: Coordinates = None) -> None:
        """
        Prints the game board with optional highlighting of player's positions, possible moves, and current location.

        Args:
            player (Player, optional): The player object. Defaults to None.
            possible_moves (List[Tuple[int, int]], optional): List of possible moves represented as tuples of coordinates. Defaults to None.
            current_loc (Coordinates, optional): The current location represented as a tuple of coordinates. Defaults to None.

        Returns:
            None
        """
        emoji_possible_moves = []
        if (possible_moves != None):
            emoji_possible_moves = self.create_emoji_moves(len(possible_moves))

        if (player != None):
            player_locs_list = player_instruments_pos.get_all_locs_4player(
                self.the_board, player)

        for i in range(len(self.the_board)):
            for j in range(len(self.the_board[0])):
                if (player != None and (i, j) in player_locs_list):
                    if (player_locs_list.index((i, j)) < 10):
                        print(
                            " "+self.pieces_nums[player_locs_list.index((i, j))], end=" ")
                    else:
                        print(
                            self.pieces_nums[player_locs_list.index((i, j))], end=" ")
                elif (current_loc != None and (i, j) == current_loc):
                    print('🎯' ,end=" ")
                elif (possible_moves != None and (i, j) in possible_moves):
                    print(
                        emoji_possible_moves[possible_moves.index((i, j))], end=" ")
                else:
                    print(self.match_cell_to_emojy(
                        self.the_board[i][j]), end=" ")
            print()

    def cell_content(self, location: Coordinates) -> BoardValues:
        """
        Returns the content of the cell at the given location on the board.

        Args:
            location (Coordinates): The coordinates of the cell on the board.

        Returns:
            BoardValues: The value stored in the cell at the given location.
        """
        return self.the_board[location[0]][location[1]]

    def is_on_board(self, location: Coordinates) -> bool:
        """
        Check if the given location is on the board (cell_content is not OUT_OF_BOARD)

        Args:
            location (Coordinates): The location to check.

        Returns:
            bool: True if the location is on the board, False otherwise.
        """
        if (0 <= location[0] < len(self.the_board)
                and 0 <= location[1] < len(self.the_board[0])
                and self.the_board[location[0]][location[1]] != BoardValues.OUT_OF_BOARD):
            return True
        return False

    def get_pieces_nums(self, triangle_length: int = 4) -> List[str]:
        """
        Returns a list of strings representing the numbers of the pieces on the board that the player can move.

        Args:
            triangle_length (int): The length of each triangle in the board. Default is 4.

        Returns:
            List[str]: The list of strings representing the numbers of the pieces.

        """
        lst = [i for i in range(1, sum(range(triangle_length+1))+1)]
        lst = [str(num) for num in lst]
        return lst

    def create_emoji_moves(self, number_of_moves: int) -> List[str]:
        """
        Creates a list of emojis representing the possible moves.

        Args:
            number_of_moves (int): The number of possible moves.

        Returns:
            List[str]: A list of emojis representing the possible moves.

        """

        return [chr(ord(START_EMOJI)+i) for i in range(number_of_moves)]
