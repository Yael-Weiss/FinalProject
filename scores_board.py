from typing import List
from player import Player


class ScoresBoard:
    """
    Represents a scores board for a game.

    Args:
        None

    Attributes:
        scores_board (dict): A dictionary that stores the scores of each player.
        just_started (bool): A flag indicating if the game has just started.
    """

    def __init__(self) -> None:
        """
        Initializes the ScoresBoard object.

        Args:
            None

        Returns:
            None
        """
        self.scores_board = {}

    def init_players_scores(self, players_list: List[Player]) -> None:
        """
        Initializes the scores of all players to 0 wins and 0 loses.

        Args:
            players_list (List[Player]): A list of Player objects representing the players in the game.

        Returns:
            None
        """
        for player in players_list:
            self.scores_board[player.name] = [0, 0]

    def set_num_of_wins(self, player_name: str, num_of_wins: int) -> None:
        """
        Sets the number of wins for a player.

        Args:
            player_name (str): The name of the player.
            num_of_wins (int): The number of wins for the player.

        Returns:
            None
        """
        self.scores_board[player_name][0] = num_of_wins

    def set_num_of_loses(self, player_name: str, num_of_loses: int) -> None:
        """
        Sets the number of loses for a player.

        Args:
            player_name (str): The name of the player.
            num_of_loses (int): The number of loses for the player.

        Returns:
            None
        """
        self.scores_board[player_name][1] = num_of_loses

    def add_winner(self, player: Player) -> None:
        """
        Increments the number of wins for a player.

        Args:
            player (Player): The Player object representing the winner.

        Returns:
            None
        """
        self.scores_board[player.name][0] += 1

    def add_loser(self, player: Player) -> None:
        """
        Increments the number of loses for a player.

        Args:
            player (Player): The Player object representing the loser.

        Returns:
            None
        """
        self.scores_board[player.name][1] += 1

    def get_str_scores(self) -> str:
        """
        Returns a string representation of the scores board.

        Args:
            None

        Returns:
            str: A string representation of the scores board.
        """
        str_scores = ""
        highest_wins = max(self.scores_board.values(), key=lambda x: x[0])
        for key, value in self.scores_board.items():
            if value == highest_wins:
                the_big_winner = key
                break
        str_scores += the_big_winner+", you won!\nThe other players scores are:\n"
        for player in self.scores_board.keys():
            str_scores += f"{player} won: " + str(
                self.scores_board[player][0]) + " times and lost: " + str(self.scores_board[player][1])+"\n"

        return str_scores
