from typing import Dict, Tuple, List

from BoardValues import BoardValues
from player import Player
from triangles import Triangles
import triangles_funcs
import unittest


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
EMOJI_NUMS = ["1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ",
              "6️⃣ ", "7️⃣ ", "8️⃣ ", "9️⃣ ", "🔟"]
EMOJI_POSSIBLE_MOVES=["😽","🐶","🦊","🐒","🐺","🐱","🐷","🐮","🦝","🐯","🐗",
                     "🐭","🐹","🐰","🐻","🫎","🐨","🐼","🐸","🦧","🐔","🐕"]


class Board:
    """

    """

    def __init__(self) -> None:
        self.the_board = self.get_empty_board()
        # self.six_corners = {Triangles.upper_tri: BoardValues.EMPTY, Triangles.lower_tri: BoardValues.EMPTY, Triangles.upper_left_tri: BoardValues.EMPTY,
        #                     Triangles.lower_left_tri: BoardValues.EMPTY, Triangles.upper_right_tri: BoardValues.EMPTY}

    def get_empty_board(self) -> List[List[BoardValues]]:
        lst = []
        temp_lst = []
        empty_places = 1
        out_of_board = 12
        while (empty_places != 5):
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

        empty_places = 13
        out_of_board = 0
        while (out_of_board != 5):

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

        empty_places = 10
        out_of_board = 3
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

        empty_places = 4
        out_of_board = 9
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
        start = 12
        for i in range(1, 5):
            for j in range(i):
                self.the_board[i-1][start+2*j] = player_color
            start -= 1
        # self.six_corners[Triangles.upper_tri] = player_color

    def fill_lower_triangle(self, player_color: BoardValues) -> None:
        start_col = 9
        places_to_fill = 4
        start_row = 13
        while (start_col != 13):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1
        # self.six_corners[Triangles.lower_tri] = player_color

    def fill_upper_left_triangle(self, player_color: BoardValues) -> None:
        start_col = 0
        places_to_fill = 4
        start_row = 4
        while (start_row != 9):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1
        # self.six_corners[Triangles.upper_left_tri] = player_color

    def fill_lower_left_triangle(self, player_color: BoardValues) -> None:
        start_col = 3
        places_to_fill = 1
        start_row = 9
        while (start_row != 13):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col -= 1
            start_row += 1
            places_to_fill += 1
        # self.six_corners[Triangles.lower_left_tri] = player_color

    def fill_upper_right_triangle(self, player_color: BoardValues) -> None:
        start_col = 18
        places_to_fill = 4
        start_row = 4
        while (start_row != 9):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col += 1
            start_row += 1
            places_to_fill -= 1
        # self.six_corners[Triangles.upper_right_tri] = player_color

    def fill_lower_right_triangle(self, player_color: BoardValues) -> None:
        start_col = 21
        places_to_fill = 1
        start_row = 9
        while (start_row != 13):
            for i in range(places_to_fill):
                self.the_board[start_row][start_col+2*i] = player_color
            start_col -= 1
            start_row += 1
            places_to_fill += 1
        # self.six_corners[Triangles.lower_right_tri] = player_color

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

    def match_cell_to_emojy(self, player_color: BoardValues):
        return EMOJY_DICT[player_color]

    def clear_screen(self) -> None:
        print("\033[H\033[J", end="")

    def print_board(self,player: Player = None, possible_moves: List[Tuple[int, int]] = None) -> None:
        if (player != None):
            player_locs_list = triangles_funcs.get_all_locs_4player(
                self.the_board, player)
            
        for i in range(len(self.the_board)):
            for j in range(len(self.the_board[0])):
                if (player != None and (i, j) in player_locs_list):
                    print(EMOJI_NUMS[player_locs_list.index((i, j))], end=" ")
                elif(possible_moves!=None and (i,j) in possible_moves):
                    print(EMOJI_POSSIBLE_MOVES[possible_moves.index((i,j))],end=" ")
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

    # def is_winner(self, player: Player, current_loc: Coordinates, go_to: Coordinates) -> bool:
    #     if (self.move_player(player, current_loc, go_to)):
    #         all_same_and_tri_name=self.is_in_triangle(player, go_to)
    #         if(all_same_and_tri_name[0] and self.six_corners[all_same_and_tri_name[1]]!=player.color):
    #             return True
    #     return False
