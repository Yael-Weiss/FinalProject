from typing import List, Tuple
from Board import Board
from BoardValues import BoardValues
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import triangles_funcs

Coordinates = Tuple[int, int]
TRIANGLES_LIST = [Triangles.upper_tri,
                  Triangles.upper_left_tri,
                  Triangles.lower_tri,
                  Triangles.lower_right_tri,
                  Triangles.lower_left_tri,
                  Triangles.upper_right_tri]
TRIANGLES_CHECK = {Triangles.upper_tri: triangles_funcs.is_loc_in_upper_tri,
                   Triangles.upper_left_tri: triangles_funcs.is_loc_in_upper_left_tri,
                   Triangles.lower_tri: triangles_funcs.is_loc_in_lower_tri,
                   Triangles.lower_right_tri: triangles_funcs.is_loc_in_lower_right_tri,
                   Triangles.lower_left_tri: triangles_funcs.is_loc_in_lower_left_tri,
                   Triangles.upper_right_tri: triangles_funcs.is_loc_in_upper_right_tri}


class MoveValidation:
    def __init__(self, game_setting: GameSettings) -> None:
        self.game_setting = game_setting

    # def get_players_destinations(self,board:Board,players_list:List[[Player]])->dict[List[[Player]],Triangles]:

    def get_list_of_possible_moves(self, location: Coordinates) -> List[Tuple[int, int]]:
        # to add jumps

        if not (self.game_setting.board.is_on_board(location)):
            return []

        lst = []
        row, col = location

        if (0 < row and 0 < col):
            if (self.game_setting.board.the_board[row-1][col-1] == BoardValues.EMPTY):
                lst.append((row-1, col-1))
        if (0 < row and col < (len(self.game_setting.board.the_board[0])-1)):
            if (self.game_setting.board.the_board[row-1][col+1] == BoardValues.EMPTY):
                lst.append((row-1, col+1))
        if (row < (len(self.game_setting.board.the_board)-1) and 0 < col):
            if (self.game_setting.board.the_board[row+1][col-1] == BoardValues.EMPTY):
                lst.append((row+1, col-1))
        if (row < (len(self.game_setting.board.the_board)-1) and col < (len(self.game_setting.board.the_board[0])-1)):
            if (self.game_setting.board.the_board[row+1][col+1] == BoardValues.EMPTY):
                lst.append((row+1, col+1))
        if (1 < col < (len(self.game_setting.board.the_board[0])-2)):
            if (self.game_setting.board.the_board[row][col-2] == BoardValues.EMPTY):
                lst.append((row, col-2))
            if (self.game_setting.board.the_board[row][col+2] == BoardValues.EMPTY):
                lst.append((row, col+2))

        return lst

    def get_set_of_possible_jumps(self, location, possible_jumps_set: set[Tuple[int, int]]) -> set[Tuple[int, int]]:
        if not (self.game_setting.board.is_on_board(location)):
            return possible_jumps_set
        row, col = location
        no_options = True
        if (self.game_setting.board.is_on_board((row-2, col-2))):
            if (self.game_setting.board.the_board[row-2][col-2] == BoardValues.EMPTY and (row-2, col-2) not in possible_jumps_set):
                possible_jumps_set.add((row-2, col-2))
                self.get_possible_jumps((row-2, col-2), possible_jumps_set)
                no_options = False

        if (self.game_setting.board.is_on_board((row-2, col+2))):
            if (self.game_setting.board.the_board[row-2][col+2] == BoardValues.EMPTY and (row-2, col+2) not in possible_jumps_set):
                possible_jumps_set.add((row-2, col+2))
                self.get_possible_jumps((row-2, col+2), possible_jumps_set)
                no_options = False

        if (self.game_setting.board.is_on_board((row+2, col-2))):
            if (self.game_setting.board.the_board[row+2][col-2] == BoardValues.EMPTY and (row+2, col-2) not in possible_jumps_set):
                possible_jumps_set.add((row+2, col-2))
                self.get_possible_jumps((row+2, col-2), possible_jumps_set)
                no_options = False

        if (self.game_setting.board.is_on_board((row+2, col+2))):
            if (self.game_setting.board.the_board[row+2][col+2] == BoardValues.EMPTY and (row+2, col+2) not in possible_jumps_set):
                possible_jumps_set.add((row+2, col+2))
                self.get_possible_jumps((row+2, col+2), possible_jumps_set)
                no_options = False

        if (self.game_setting.board.is_on_board((row, col+2))):
            if (self.game_setting.board.the_board[row][col+2] == BoardValues.EMPTY and (row, col+2) not in possible_jumps_set):
                possible_jumps_set.add((row, col+2))
                self.get_possible_jumps((row, col+2), possible_jumps_set)
                no_options = False

        if (self.game_setting.board.is_on_board((row, col-2))):
            if (self.game_setting.board.the_board[row][col-2] == BoardValues.EMPTY and (row, col-2) not in possible_jumps_set):
                possible_jumps_set.add((row, col-2))
                self.get_possible_jumps((row, col-2), possible_jumps_set)
                no_options = False

        if (no_options):
            return possible_jumps_set

    def is_in_destination(self,player:Player,loc:Coordinates)->bool:
        return TRIANGLES_CHECK[player.destination_tri](loc)

    def is_in_triangle_not_des(player:Player, loc: Coordinates) -> bool:
        for tri in TRIANGLES_CHECK.keys():
            if(player.destination_tri!=tri):
                if(TRIANGLES_CHECK[tri](loc)):
                    return True
        return False

    def is_valid_move(self, player: Player, loc: Coordinates, go_to: Coordinates) -> bool:
        if ((not self.is_in_triangle_not_des(player,go_to)) and player.color == self.cell_content(loc)
                    and (go_to in self.get_possible_moves(loc) or go_to in self.get_possible_jumps(loc, {}))):
                return True
        return False

    def move_player(self, player: Player, loc: Coordinates, go_to: Coordinates) -> bool:
        if (self.is_valid_move(player, loc, go_to)):
            self.the_board[loc[0]][loc[1]] = BoardValues.EMPTY
            self.the_board[go_to[0]][go_to[1]] == player.color
            return True
        return False
