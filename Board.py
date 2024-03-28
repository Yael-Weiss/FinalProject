from typing import Dict, Tuple, List

from BoardValues import BoardValues
from player import Player
from triangles import Triangles
import triangles_funcs


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
EMOJI_POSSIBLE_MOVES = ["😽" ,"🐶","🦊","🐒", "🐺" ,"🐱","🐷","🐮", "🦝","🐯","🐗",
                        "🐭" ,"🐹","🐰","🐻", "🫎" ,"🐨","🐼","🐸", "🦧" ,"🐔","🐕","🐩",
                        "🦛" ,"🦥","🦖","🐬", "🦭" ,"🐓","💩","🐖", "🦐" ,"🦑","🦆","🦀","🦞"]


class Board:
    """

    """
  

    def __init__(self,triangle_length:int=4) -> None:
        self.TRIANGLE_LENGTH = triangle_length
        self.EMOJI_NUMS=self.get_emoji_nums(self.TRIANGLE_LENGTH)
        self.BOARD_LENGTH = self.TRIANGLE_LENGTH*4+1
        self.BOARD_WIDTH = self.TRIANGLE_LENGTH*6+1
        self.the_board = self.get_empty_board()

    def get_emoji_nums(self,trianlge_length:int=4)->List[str]:
        lst=[i for i in range(1,sum(range(trianlge_length+1))+1)]
        lst=[str(num) for num in lst]
        return lst

    def get_empty_board(self) -> List[List[BoardValues]]:
        lst = []
        temp_lst = []
        empty_places = 1
        out_of_board = self.BOARD_WIDTH//2
        while (empty_places != self.TRIANGLE_LENGTH+1):
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

        empty_places = self.BOARD_WIDTH//2+1
        out_of_board = 0
        while (out_of_board != self.TRIANGLE_LENGTH+1):

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

        empty_places = self.TRIANGLE_LENGTH*2+2
        out_of_board = self.TRIANGLE_LENGTH-1
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

        empty_places = self.TRIANGLE_LENGTH
        out_of_board = (self.TRIANGLE_LENGTH*2)+1
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
        start = self.BOARD_WIDTH//2
        for i in range(1, 1+self.TRIANGLE_LENGTH):
            for j in range(i):
                self.the_board[i-1][start+2*j] = player_color
            start -= 1

    def fill_lower_triangle(self, player_color: BoardValues) -> None:
        start_col = (2*self.TRIANGLE_LENGTH)+1
        places_to_fill = self.TRIANGLE_LENGTH
        start_row = self.BOARD_LENGTH-self.TRIANGLE_LENGTH
        stop_while = (start_col+self.TRIANGLE_LENGTH)
        while (start_col != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1
            
    def fill_upper_left_triangle(self, player_color: BoardValues) -> None:
        start_col = 0
        places_to_fill = self.TRIANGLE_LENGTH
        start_row = self.TRIANGLE_LENGTH
        stop_while = ((start_row+self.TRIANGLE_LENGTH)+1)
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1

    def fill_lower_left_triangle(self, player_color: BoardValues) -> None:
        start_col = self.TRIANGLE_LENGTH-1
        places_to_fill = 1
        start_row = (self.TRIANGLE_LENGTH*2+1)
        stop_while = start_row+self.TRIANGLE_LENGTH
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col -= 1
            start_row += 1
            places_to_fill += 1

    def fill_upper_right_triangle(self, player_color: BoardValues) -> None:
        start_col = (self.TRIANGLE_LENGTH*4)+2
        places_to_fill = self.TRIANGLE_LENGTH
        start_row = self.TRIANGLE_LENGTH
        stop_while=(self.TRIANGLE_LENGTH*2+1)
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1

    def fill_lower_right_triangle(self, player_color: BoardValues) -> None:
        start_col = ((self.TRIANGLE_LENGTH*4)+2+(self.TRIANGLE_LENGTH-1))
        places_to_fill = 1
        start_row = (self.TRIANGLE_LENGTH*2+1)
        stop_while=start_row+self.TRIANGLE_LENGTH
        while (start_row != stop_while):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col -= 1
            start_row += 1
            places_to_fill += 1

    def fill_beginning_triangles(self, players_list: List[Player]) -> None:
        # to think about dicts
        for player in players_list:
            if (player.starting_tri == Triangles.upper_tri):
                self.fill_upper_triangle(player.color)
            if (player.starting_tri == Triangles.upper_left_tri):
                self.fill_upper_left_triangle(player.color)
            if (player.starting_tri == Triangles.upper_right_tri):
                self.fill_upper_right_triangle(player.color)
            if (player.starting_tri == Triangles.lower_right_tri):
                self.fill_lower_right_triangle(player.color)
            if (player.starting_tri == Triangles.lower_tri):
                self.fill_lower_triangle(player.color)
            if (player.starting_tri == Triangles.lower_left_tri):
                self.fill_lower_left_triangle(player.color)

    def set_triangle_length(self,tri_length:int):
        self.TRIANGLE_LENGTH=tri_length

    def match_cell_to_emojy(self, player_color: BoardValues):
        return EMOJY_DICT[player_color]

    def clear_screen(self) -> None:
        print("\033[H\033[J", end="")

    def print_board(self, player: Player = None, possible_moves: List[Tuple[int, int]] = None, current_loc: Coordinates = None) -> None:
        if (player != None):
            player_locs_list = triangles_funcs.get_all_locs_4player(
                self.the_board, player)

        for i in range(len(self.the_board)):
            for j in range(len(self.the_board[0])):
                if (player != None and (i, j) in player_locs_list):
                    if(player_locs_list.index((i, j))<10):
                        print(" "+self.EMOJI_NUMS[player_locs_list.index((i, j))], end=" ")
                    else:
                        print(self.EMOJI_NUMS[player_locs_list.index((i, j))], end=" ")
                elif (current_loc != None and (i, j) == current_loc):
                    print("🎯",end=" ")
                elif (possible_moves != None and (i, j) in possible_moves):
                    print(
                        EMOJI_POSSIBLE_MOVES[possible_moves.index((i, j))], end=" ")
                else:
                    print(self.match_cell_to_emojy(
                        self.the_board[i][j]), end=" ")
            print()

    def cell_content(self, location: Coordinates) -> BoardValues:
        return self.the_board[location[0]][location[1]]

    def is_on_board(self, location: Coordinates) -> bool:
        if (0 <= location[0] < len(self.the_board)
                and 0 <= location[1] < len(self.the_board[0])
                and self.the_board[location[0]][location[1]] != BoardValues.OUT_OF_BOARD):
            return True
        return False


