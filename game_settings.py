from typing import List

from board2 import Board
from board_values import BoardValues
from player import Player
from scores_board import ScoresBoard
from triangles import Triangles
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
    """
    The GameSettings class represents the settings for a Chinese Checkers game.
    It includes methods to initialize the game board, players, and scores.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the GameSettings class.
        """
        self.board = None
        self.players_list = []
        self.score_board = ScoresBoard()

    def init_only_board(self, triangle_length: int = 4) -> None:
        """
        Initializes the game board and fill the relevant triangles.

        Args:
            triangle_length (int): The length of each triangle in the board.

        Returns:
            None
        """
        self.board = Board(triangle_length)
        self.board.fill_beginning_triangles(self.players_list)

    def init_board(self) -> None:
        """
        Initializes the game board with triangles, players, and scores.
        The function gets most of the data from the user.

        Returns:
            None
        """
        self.players_list = self.get_all_players_list()
        self.board = Board(int(self.get_tri_size()))
        self.board.the_board = self.board.get_empty_board()
        self.board.fill_beginning_triangles(self.players_list)
        self.score_board.init_players_scores(self.players_list)

    def no_more_player_same_name(self, name: str, players_list: List[Player]) -> bool:
        """
        Checks if there are no other players with the same name.

        Args:
            name (str): The name of the player to check.
            players_list (List[Player]): The list of players to compare against.

        Returns:
            bool: True if there are no other players with the same name, False otherwise.
        """
        if (name == ""):
            return False
        if (players_list == []):
            return True

        for player in players_list:
            if player.name == name:
                return False
        return True

    def get_remaining_colors(self, real_players_list: List[Player]) -> List[BoardValues]:
        """
        Gets the list of remaining colors that can be assigned to players.

        Args:
            real_players_list (List[Player]): The list of real players.

        Returns:
            List[BoardValues]: The list of remaining colors.
        """
        colors_list = list(COLORS_DICT.values())
        for player in real_players_list:
            colors_list.remove(player.color)
        return colors_list

    def is_valid_name(self, player_name, real_players_lst) -> bool:
        """
        Checks if a player name is valid.

        Args:
            player_name (str): The name of the player to check.
            real_players_lst (List[Player]): The list of real players.

        Returns:
            bool: True if the player name is valid, False otherwise.
        """
        if (not self.no_more_player_same_name(player_name, real_players_lst)) or (player_name == "") or (self.str_is_only_spaces(player_name)) or ("_" in player_name) or (len(player_name.split(" ")) > 1):
            return False
        return True

    def str_is_only_spaces(self, name: str) -> bool:
        """
        Checks if a string consists of only spaces.

        Args:
            name (str): The string to check.

        Returns:
            bool: True if the string consists of only spaces, False otherwise.
        """
        for i in name:
            if (i != " "):
                return False
        return True

    def get_colors_list(self) -> List[BoardValues]:
        """
        Gets the list of available colors for players.

        Returns:
            List[BoardValues]: The list of available colors.
        """
        COLORS_LIST = [(b, b.name) for b in BoardValues]
        COLORS_LIST.remove((BoardValues.EMPTY, BoardValues.EMPTY.name))
        COLORS_LIST.remove(
            (BoardValues.OUT_OF_BOARD, BoardValues.OUT_OF_BOARD.name))
        return COLORS_LIST

    def get_tri_size(self)->int:
        """
        Gets the size of the game board from the user.

        Returns:
            int: The size of the game board.
        """
        while(True):
            tri_size = input_provider.get_input_dialog("""What size you want the board? 
                                            \nIt is recommended to choose a number between 2-10. 
                                            \nYou can choose a bigger one if you have a big screen.""")
            while True:
                if (tri_size.isdigit()):
                    if(1 < int(tri_size)<13):
                        break
                    else:
                        tri_size = input_provider.get_input_dialog("""Let's be honest, your screen is not so big and your computer is not so strong, please try again. 
                                                            \nWhat size you want the board? 
                                                \nIt is recommended to choose a number between 2-10. 
                                                \nYou can choose a bigger one if you have a big screen and strong computer.""")    
                else:        
                    tri_size = input_provider.get_input_dialog("""Invalid input, try again. 
                                                            \nWhat size you want the board? 
                                                \nIt is recommended to choose a number between 2-10. 
                                                \nYou can choose a bigger one if you have a big screen and strong computer.""")
            input_provider.print_message_dialog("In the next window you'll see an empty board. \nThe board will be in size "+tri_size+" as you chose.\nPlease ensure that this is the size of the board that you want.","Let's see the board")
            temp_board = Board(int(tri_size))
            temp_board.get_empty_board()
            temp_board.clear_screen()
            temp_board.print_board()
            input("Press click enter to continue")
            temp_board.clear_screen()
            ensuring_message = "You chose the board to be in size "+tri_size+". \nDo you want to continue with this size?"
            if(input_provider.make_yes_no_dialog("Chinese Checkers Game",ensuring_message , "Yes", "No")):
                break

        return int(tri_size)

    def get_num_of_players_and_comps(self) -> int:
        """
        Gets the number of computer players and real players from the user.

        Returns:
            Tuple[int, int]: The number of real players and computer players.
        """
        possible_num_of_players = []
        for x in range(POSSIBLE_NUM_OF_PLAYERS):
            possible_num_of_players.append((x, str(x)))

        num_of_comp_players = input_provider.get_input_in_radiolist_dialog("""You did the best choice and decided to play Chinese Checkers Game! 
                                                                           \nSo let's start.
                                                                            \nThe game fits for 2-6 players. 
                                                                           \nHow many computer players would you like in the game? 
                                                                           \n(In the next window you will enter the details of the real players)""",
                                                                           possible_num_of_players)
        if (num_of_comp_players == None):
            self.get_num_of_players_and_comps()

        possible_num_of_real_players = []
        start = 1
        if (num_of_comp_players == 0):
            start = 2
        for i in range(start, POSSIBLE_NUM_OF_PLAYERS-num_of_comp_players+1):
            possible_num_of_real_players.append((i, str(i)))

        num_of_real_players = input_provider.get_input_in_radiolist_dialog("How many real players would like to play? ",
                                                                           possible_num_of_real_players)
        return num_of_real_players, num_of_comp_players

    def get_comp_players(self, num_of_comp_players: int, total_num_of_players: int, real_players_list: List[Player]) -> List[Player]:
        """
        initialize the list of computer players.

        Args:
            num_of_comp_players (int): The number of computer players.
            total_num_of_players (int): The total number of players.
            real_players_list (List[Player]): The list of real players.

        Returns:
            List[Player]: The list of computer players.
        """
        comp_players = []
        colors_list = self.get_remaining_colors(real_players_list)
        for i in range(num_of_comp_players):
            player_name = f"Computer#{i+1}"
            player_color = colors_list[i]
            player = Player(player_name, player_color, TRIANGLES_DICT[total_num_of_players][len(
                real_players_list)+i], True)
            comp_players.append(player)
        return comp_players

    def get_valid_player_name(self,player_number:int, real_players_lst: List[Player]) -> str:
        """
        ask the user for a valid name for a player.

        Args:
            player_number (int): The number of the player.
            real_players_lst (List[Player]): The list of real players.

        Returns:
            str: The valid name for the player.
        """
        player_name = input_provider.get_input_dialog(
            f"""What is the name of the player number #{player_number}?: \n
                    Please don't use "_" in the name. \nThe name has to be one word. \n""")
        while (True):
            while (True):
                if (player_name == "" or self.str_is_only_spaces(player_name)):
                    player_name = input_provider.get_input_dialog(
                        f"You didn't enter a name, please choose one.\nPlease choose a name for the player number #{player_number}?: \n")
                elif ("_" in player_name):
                    player_name = input_provider.get_input_dialog(
                        f"""Please don't use "_" in the name. \n
                            What is the name of the player number #{player_number}?: \n""")
                elif (len(player_name.split(" ")) > 1):
                    player_name = input_provider.get_input_dialog(
                        f"""The name has to be one word. \n
                            What is the name of the player number #{player_number}?: \n""")
                elif (not self.no_more_player_same_name(player_name, real_players_lst)):
                    player_name = input_provider.get_input_dialog(
                        f"""There's already a player with this name, please choose different one. \n
                        Please don't use "_" in the name. \n
                        What is the name of the player number #{player_number}?: \n""")
                else:
                    break
            if (self.is_valid_name(player_name, real_players_lst)):
                break
        return player_name

    def get_real_players_list(self, num_of_real_players: int, total_num_players: int) -> List[Player]:
        """
        initialize the list of real players.

        Args:
            num_of_real_players (int): The number of real players.
            total_num_players (int): The total number of players.

        Returns:
            List[Player]: The list of real players.
        """
        real_players_lst = []
        COLORS_LIST = self.get_colors_list()
        for j in range(num_of_real_players):
            player_name = self.get_valid_player_name(j+1,real_players_lst)
            player_color = input_provider.get_input_in_radiolist_dialog(
                f"Hello {player_name}, What color would you like to be?", COLORS_LIST)

            player = Player(player_name, player_color,
                            TRIANGLES_DICT[total_num_players][j])
            real_players_lst.append(player)
            COLORS_LIST.remove((player_color, player_color.name))
        return real_players_lst

    def get_all_players_list(self) -> List[Player]:
        """
        Gets the list of all players.

        Returns:
            List[Player]: The list of all players.
        """
        num_of_real_players, num_of_comp_players = self.get_num_of_players_and_comps()
        real_players_list = self.get_real_players_list(
            num_of_real_players, num_of_real_players+num_of_comp_players)
        comp_player_list = self.get_comp_players(num_of_comp_players,
                                                 num_of_real_players+num_of_comp_players, real_players_list)
        return real_players_list+comp_player_list

