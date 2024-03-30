from typing import List, Tuple
from board_values import BoardValues
from player import Player
from game_settings import GameSettings
from triangles import Triangles
import move_validation

COLORS = {
    "BoardValues.RED": BoardValues.RED,
    "BoardValues.BLUE": BoardValues.BLUE,
    "BoardValues.YELLOW": BoardValues.YELLOW,
    "BoardValues.PURPLE": BoardValues.PURPLE,
    "BoardValues.GREEN": BoardValues.GREEN,
    "BoardValues.ORANGE": BoardValues.ORANGE
}
TRIANGLES = {
    "Triangles.upper_tri": Triangles.upper_tri,
    "Triangles.lower_tri": Triangles.lower_tri,
    "Triangles.upper_left_tri": Triangles.upper_left_tri,
    "Triangles.lower_left_tri": Triangles.lower_left_tri,
    "Triangles.upper_right_tri": Triangles.upper_right_tri,
    "Triangles.lower_right_tri": Triangles.lower_right_tri
}


def from_str_to_coordinates(str: str) -> tuple[int, int]:
    """
    Converts a string representation of coordinates to a tuple of integers.

    Args:
        str (str): The string representation of coordinates in the format "(x, y)".

    Returns:
        tuple[int, int]: A tuple containing the x and y coordinates as integers.
    """
    coma_index = str.find(",")
    num1 = str[1:coma_index]
    num2 = str[coma_index+1:len(str)-1]
    return (int(num1), int(num2))

def read_and_load_log_file(file_name: str) -> Tuple[GameSettings, bool]:
    """
    Reads and loads a log file containing game data.

    Args:
        file_name (str): The name of the log file to read.

    Returns:
        Tuple[GameSettings, bool]: A tuple containing the game settings and a boolean value indicating if it is the first game on the tournament or not.
        false if it is the first game, True otherwise.
    """
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    # Extract players list
    last_line_of_players = lines.index("")
    lines_for_players_list = lines[1:last_line_of_players]
    players_list = get_players_list_from_log(lines_for_players_list)
    
    # Extract triangle length
    triangle_length_line = lines[last_line_of_players+1].split(":")
    triangle_length = int(triangle_length_line[1])

    # Extract scores lines
    index_of_scores = -1
    moves_lines = []
    scores_lines = []

    for k in range(len(lines)-1, -1, -1):
        if ("The other players scores are:" == lines[k]):
            index_of_scores = k
            scores_lines = lines[k:len(lines)]
            if "" in scores_lines:
                last_line_of_scores = scores_lines.index("")
                scores_lines = scores_lines[1:last_line_of_scores]
            break

    # Extract moves lines
    for j in range(len(lines)-1, index_of_scores, -1):
        if ("These are the moves:" == lines[j]):
            moves_lines = lines[j:]
            if "" in moves_lines:
                last_line_of_moves = moves_lines.index("")
                moves_lines = moves_lines[1:last_line_of_moves]
            break
    
    return get_game_settings_from_log(scores_lines, moves_lines, players_list, triangle_length)

def get_players_list_from_log(lines: List[str]) -> list[Player]:
    """
    Converts a list of log lines into a list of Player objects.

    Args:
        lines (List[str]): A list of log lines.

    Returns:
        list[Player]: A list of Player objects.
    """
    players_list = []
    for index in range(0, len(lines), 5):
        players_list.append(Player(lines[index],
                                   COLORS[lines[index+1]],
                                   TRIANGLES[lines[index+3]],
                                   lines[index+2] == "True"))
    return players_list

def get_game_settings_from_log(scores_lines: List[str], moves_lines: List[str], players_list: List[Player], triangle_length: int = 4) -> Tuple[GameSettings, bool]:
    """
    Retrieves game settings from log files and returns a tuple containing the game settings and a boolean value.

    Args:
        scores_lines (List[str]): A list of strings representing the scores from the log file.
        moves_lines (List[str]): A list of strings representing the moves from the log file.
        players_list (List[Player]): A list of Player objects representing the players in the game.
        triangle_length (int, optional): The length of the triangle board. Defaults to 4.

    Returns:
        Tuple[GameSettings, bool]: A tuple containing the game settings and a boolean value. The boolean value indicates whether 
        it is the first game on the tournament or not. False if it is the first game, True otherwise.
    """
    game_settings = GameSettings()
    game_settings.players_list = players_list
    game_settings.init_only_board(triangle_length)
    game_settings.score_board.init_players_scores(game_settings.players_list)
    set_scores_board_from_log(scores_lines, game_settings)
    
    if moves_lines == []:
        return (game_settings, True)
    set_moves_and_move_from_log(moves_lines[1:], game_settings)
    return (game_settings, False)

def set_moves_and_move_from_log(moves_lines: List[str], game_settings: GameSettings) -> None:
    """
    Sets the moves and moves the players based on the log.

    Args:
        moves_lines (List[str]): A list of strings representing the moves in the log.
        game_settings (GameSettings): The game settings object.

    Returns:
        None
    """
    players_list = game_settings.players_list
    for line in moves_lines:
        splited_line = line.split("_")
        for i in range(len(players_list)):
            if players_list[i].name == splited_line[1]:
                player_to_move = players_list[i]
        current_loc = from_str_to_coordinates(splited_line[2])
        go_to = from_str_to_coordinates(splited_line[3])
        move_validation.move_player(
            game_settings, player_to_move, current_loc, go_to)

def set_scores_board_from_log(scores_lines: List[str], game_settings: GameSettings) -> None:
    """
    Updates the score board based on the scores recorded in the log.

    Args:
        scores_lines (List[str]): A list of strings representing the scores recorded in the log.
        game_settings (GameSettings): An instance of the GameSettings class.

    Returns:
        None
    """
    players_list = game_settings.players_list
    for line in scores_lines:
        splited_line = line.split(" ")
        for player in players_list:
            if player.name == splited_line[0]:
                player_name = player.name
                game_settings.score_board.set_num_of_wins(
                    player_name, int(splited_line[2]))
                game_settings.score_board.set_num_of_loses(
                    player_name, int(splited_line[6]))


