from typing import Dict, Tuple, List


from board import Board
from BoardValues import BoardValues
from player import Player
from triangles import Triangles
import triangles_funcs
import input_provider

TRIANGLES_DICT = {2: [Triangles.upper_tri, Triangles.lower_tri],
                  3: [Triangles.upper_tri, Triangles.lower_left_tri, Triangles.lower_right_tri],
                  4: [Triangles.upper_tri, Triangles.upper_left_tri, Triangles.lower_tri, Triangles.lower_right_tri],
                  5: [Triangles.upper_tri, Triangles.upper_left_tri, Triangles.lower_tri, Triangles.lower_right_tri, Triangles.lower_left_tri],
                  6: [Triangles.upper_tri, Triangles.upper_left_tri, Triangles.lower_tri, Triangles.lower_right_tri, Triangles.lower_left_tri, Triangles.upper_right_tri]}


COLORS_DICT = {BoardValues.RED.name: BoardValues.RED,
               BoardValues.BLUE.name: BoardValues.BLUE,
               BoardValues.YELLOW.name: BoardValues.YELLOW,
               BoardValues.PURPLE.name: BoardValues.PURPLE,
               BoardValues.GREEN.name: BoardValues.GREEN,
               BoardValues.ORANGE.name: BoardValues.ORANGE}
POSSIBLE_NUM_OF_PLAYERS = 6


class GameSettings:
    def __init__(self) -> None:
        self.board = Board()
        self.players_list = []
    
    def init_board(self) -> None:
        self.players_list = self.get_all_players_list()
        self.board.fill_beginning_triangles(self.players_list)

    def no_more_player_same_name(self, name: str, players_list: List[Player]) -> bool:
        if (name == ""):
            return False
        if (players_list == []):
            return True

        for player in players_list:
            if player.name == name:
                return False
        return True

    def get_remaining_colors(self, real_players_list: List[Player]) -> List[BoardValues]:
        colors_list = list(COLORS_DICT.values())
        for player in real_players_list:
            colors_list.remove(player.color)
        return colors_list

    def get_comp_players(self, num_of_comp_players: int, total_num_of_players: int, real_players_list: List[Player]) -> List[Player]:
        comp_players = []
        colors_list = self.get_remaining_colors(real_players_list)
        for i in range(num_of_comp_players):
            player_name = f"Computer #{i+1}"
            player_color = colors_list[i]
            player = Player(player_name, player_color, TRIANGLES_DICT[total_num_of_players][len(
                real_players_list)+i], True)
            comp_players.append(player)
        return comp_players

    def get_list_all_players(self, real_players_list: List[Player], comp_players: List[Player]) -> List[Player]:
        all_players = real_players_list + comp_players
        return all_players

    def get_num_of_players_and_comps(self) -> int:
        possible_num_of_players = []
        for x in range(POSSIBLE_NUM_OF_PLAYERS):
            possible_num_of_players.append((x, str(x)))

        num_of_comp_players = input_provider.get_input_in_radiolist_dialog("""You did the best choice and decided to play Chinese Checkers Game! 
                                                                           \nSo let's start.
                                                                            \nThe game fits for 2-6 players. 
                                                                           \nHow many computer players would you like in the game? 
                                                                           \n(In the next window you will enter the details of the real players)""",
                                                                           possible_num_of_players)

        possible_num_of_real_players = []
        for i in range(1,POSSIBLE_NUM_OF_PLAYERS-num_of_comp_players+1):
            possible_num_of_real_players.append((i, str(i)))

        num_of_real_players = input_provider.get_input_in_radiolist_dialog("How many real players would like to play? ",
                                                                           possible_num_of_real_players)
        return num_of_real_players,num_of_comp_players
    
    def get_colors_list(self) -> List[BoardValues]:
        COLORS_LIST = [(b, b.name) for b in BoardValues]
        COLORS_LIST.remove((BoardValues.EMPTY, BoardValues.EMPTY.name))
        COLORS_LIST.remove(
            (BoardValues.OUT_OF_BOARD, BoardValues.OUT_OF_BOARD.name))
        return COLORS_LIST
    
    def get_real_players_list(self, num_of_real_players: int,total_num_players:int) -> List[Player]:
        real_players_lst = []
        COLORS_LIST = self.get_colors_list()
        for j in range(num_of_real_players):
            player_name = input_provider.get_input_dialog(
                f"What is the name of the player number #{j+1}?: \n")

            while (True):
                if (self.no_more_player_same_name(player_name, real_players_lst)):
                    break
                if (player_name == ""):
                    player_name = input_provider.get_input_dialog(
                        f"You didn't enter a name, please choose one.\nPlease choose a name for the player number #{j+1}?: \n")
                else:
                    player_name = input_provider.get_input_dialog(
                        f"There's already a player with this name, please choose different one. \nWhat is the name of the player number #{j+1}?: \n")

            player_color = input_provider.get_input_in_radiolist_dialog(
                f"Hello {player_name}, What color would you like to be?", COLORS_LIST)
            # print(f"name:{player_name}, color:{player_color}")
            player = Player(player_name, player_color,
                            TRIANGLES_DICT[total_num_players][j])
            real_players_lst.append(player)
            COLORS_LIST.remove((player_color, player_color.name))
        return real_players_lst
    
    def get_all_players_list(self) -> List[Player]:
        num_of_real_players,num_of_comp_players = self.get_num_of_players_and_comps()
        real_players_list=self.get_real_players_list(num_of_real_players,num_of_real_players+num_of_comp_players)
        comp_player_list = self.get_comp_players(num_of_comp_players,
                                                 num_of_real_players+num_of_comp_players, real_players_list)
        return real_players_list+comp_player_list


if __name__ == "__main__":
    # happens in main
    GameSettings.set_name("file.name")

    # happens in single turn
    GameSettings.say_hello()
    pass
