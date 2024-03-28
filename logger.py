from typing import List, Tuple
from datetime import datetime
from player import Player

Coordinates = Tuple[int, int]


class Logger:
    """
    The Logger class is responsible for logging game information to a file.
    """
    def intro_4_new_game(file_name: str, players_list: List[Player], triangle_length: int) -> None:
        """
        Writes the tournament log for a new game.

        Args:
            file_name (str): The name of the log file.
            players_list (List[Player]): A list of Player objects representing the players in the game.
            triangle_length (int): Represents the board size.

        Returns:
            None
        """
        time = datetime.now().strftime("%Y-%m-%d") + " " + \
            datetime.now().strftime("%H:%M:%S")
        with open(Logger.name, 'w') as f:
            f.write(time + " Tournament log - These are the players:\n")
            for player in players_list:
                f.write(player.name + "\n" + str(player.color) + "\n" + str(player.is_comp) +
                        "\n" + str(player.starting_tri) + "\n" + str(player.destination_tri) + "\n")
            f.write("\nTriangleLength:" + str(triangle_length) + "\n")

    def create_file(file_name: str, players_list: List[Player], triangle_length: int = 4) -> None:
        """
        Create a file with the given file name and write the introduction for a new game.

        Args:
            file_name (str): The name of the file to be created.
            players_list (List[Player]): A list of Player objects representing the players in the game.
            triangle_length (int, optional): Represents the board size. Defaults to 4.

        Returns:
            None
        """
        Logger.name = file_name + ".txt"
        Logger.intro_4_new_game(file_name, players_list, triangle_length)

    def start_new_game_log(another_game: bool) -> None:
        """
        Start a new game log.

        Args:
            another_game (bool): Indicates whether it is another game or not.

        Returns:
            None
        """
        with open(Logger.name, 'a') as f:
            if another_game:
                f.write("\nNew Game: \n" + "These are the moves:\n")

    def add_message(player_name: str, current_loc: Coordinates, go_to: Coordinates) -> None:
        """
        Adds a message to the logger file.

        Args:
            player_name (str): The name of the player.
            current_loc (Coordinates): The current location of the player.
            go_to (Coordinates): The location the player is going to.

        Returns:
            None
        """
        time = datetime.now().strftime("%Y-%m-%d") + " " + datetime.now().strftime("%H:%M:%S")
        message = time + f"_{player_name}_{current_loc}_{go_to}"
        with open(Logger.name, 'a') as f:
            f.write(message + '\n')

    def add_scores_message(scores_message: str) -> None:
        """
        Appends a message with the scores to the log file.

        Args:
            scores_message (str): The message to be added to the log file.

        Returns:
            None
        """
        with open(Logger.name, 'a') as f:
            f.write("\n"+scores_message)  # + '\n\n')
