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
        
    def init_board(self)->None:
        self.players_list = self.get_players_list()
        self.board.fill_beginning_triangles(self.players_list)

    def get_players_list(self):# -> List[Player]:
        #create color dict/ for run on BoardValues
        players_lst = []
        num_of_players=input_provider.get_input_in_radiolist_dialog("How many players would like to play? the game fits for 2-6 players.",
                                                        [(2,"2"),(3,"3"),(4,"4"),(5, "5"), (6,"6")])
        
        COLORS_LIST=[(b,b.name) for b in BoardValues]   
        COLORS_LIST.remove((BoardValues.EMPTY,BoardValues.EMPTY.name))
        COLORS_LIST.remove((BoardValues.OUT_OF_BOARD,BoardValues.OUT_OF_BOARD.name))     
        for j in range(num_of_players):
            name_player=input_provider.get_input_dialog(f"What is the name of the player number #{j+1}?: \n")
            color_player = input_provider.get_input_in_radiolist_dialog(f"Hello {name_player}, What color would you like to be?",COLORS_LIST)
            print(f"name:{name_player}, color:{color_player}")
            player = Player(name_player, color_player, TRIANGLES_DICT[num_of_players][j])
            players_lst.append(player)
            COLORS_LIST.remove((color_player,color_player.name))
        return players_lst        


if __name__ == "__main__":
    game=GameSettings()
    game.get_players_list()