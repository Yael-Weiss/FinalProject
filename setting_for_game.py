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


class GameSettings:
    def __init__(self) -> None:
        self.board = Board()
        self.players_list = []

    def init_board(self) -> None:
        self.players_list = self.get_players_list()
        self.board.fill_beginning_triangles(self.players_list)

    def no_more_player_same_name(self,name: str, players_list: List[Player]) -> bool:
        if(name == ""):
            return False 
        if(players_list == []):
            return True
           
        for player in players_list:
            if player.name == name:
                return False
        return True

    def get_players_list(self):  # -> List[Player]:
        # create color dict/ for run on BoardValues
        players_lst = []
        num_of_players = input_provider.get_input_in_radiolist_dialog("How many players would like to play? the game fits for 2-6 players.",
                                                                      [(2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6")])

        COLORS_LIST = [(b, b.name) for b in BoardValues]
        COLORS_LIST.remove((BoardValues.EMPTY, BoardValues.EMPTY.name))
        COLORS_LIST.remove(
            (BoardValues.OUT_OF_BOARD, BoardValues.OUT_OF_BOARD.name))
        for j in range(num_of_players):
            player_name = input_provider.get_input_dialog(
                    f"What is the name of the player number #{j+1}?: \n")
            
            while (True):
                if (self.no_more_player_same_name(player_name, players_lst)):
                    break
                if(player_name == ""):
                    player_name = input_provider.get_input_dialog(f"You didn't enter a name, please choose one.\nPlease choose a name for the player number #{j+1}?: \n")
                else:
                    player_name = input_provider.get_input_dialog(f"There's already a player with this name, please choose different one. \nWhat is the name of the player number #{j+1}?: \n")
                
            player_color = input_provider.get_input_in_radiolist_dialog(
                f"Hello {player_name}, What color would you like to be?", COLORS_LIST)
            print(f"name:{player_name}, color:{player_color}")
            player = Player(player_name, player_color,
                            TRIANGLES_DICT[num_of_players][j])
            players_lst.append(player)
            COLORS_LIST.remove((player_color, player_color.name))
        return players_lst


if __name__ == "__main__":
    # game=GameSettings()
    # game.get_players_list()
    pass
