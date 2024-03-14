from typing import Dict, Tuple, List


from Board import Board
from BoardValues import BoardValues
from player import Player
from triangles import Triangles
import triangles_funcs

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

    def get_players_list(self) -> List[Player]:
        #creat color dict/ for run on BoardValues
        players_lst = []
        num_of_players = input("How many players would like to play? the game fits for 2-6 players.\n")
        while (True):  # checks that num_of_players got a valid input
            if(str(num_of_players).isdigit()):
                if (1 <= int(num_of_players) <= 6):  # to enter maxnumofplayers
                    break
            num_of_players = input(
                "Invalid input. Let's try again, how many players would like to play? \n")
        
        num_of_players = int(num_of_players)
        for i in range(num_of_players):
            colors_str = ', '.join(COLORS_DICT.keys())
            name_player = input(
                f"What is the name of the player number #{i+1}?: \n")
            color_player = input(
                f"What color would you like to be? please choose one of the next options: {colors_str} \n")
            while (True):
                if (color_player in COLORS_DICT.keys()):
                    break
                color_player = input(
                    f"Invalid input. What color would you like to be? please choose one of the next options: {colors_str}\n")
            player = Player(name_player, COLORS_DICT[color_player], TRIANGLES_DICT[num_of_players][i])
            players_lst.append(player)
            COLORS_DICT.pop(color_player)
        return players_lst        


if __name__ == "__main__":
    board = Board()
    game = GameSettings(board)

    board.fill_upper_triangle(BoardValues.RED)
    board.fill_lower_triangle(BoardValues.BLUE)
    board.fill_upper_left_triangle(BoardValues.GREEN)
    board.fill_lower_left_triangle(BoardValues.ORANGE)
    board.fill_upper_right_triangle(BoardValues.PURPLE)
    board.fill_lower_right_triangle(BoardValues.YELLOW)
    board.print_board()
    print(board.six_corners)
    # board.clear_screen()
    # board.print_board()
    # print(", ".join(game.players_list))
    # print(BoardValues["RED"].value)
