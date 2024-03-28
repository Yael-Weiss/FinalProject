from typing import List, Tuple
from BoardValues import BoardValues
from board import Board
from logger import Logger
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import moveValidation
from scores_board import ScoresBoard

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
    coma_index = str.find(",")
    num1 = str[1:coma_index]
    num2 = str[coma_index+1:len(str)-1]
    return (int(num1), int(num2))


def read_and_load_log_file(file_name: str) -> Tuple[GameSettings,bool]:
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    last_line_of_players = lines.index("")
    lines_for_players_list = lines[1:last_line_of_players]
    players_list = get_players_list_from_log(lines_for_players_list)
    triangle_length_line = lines[last_line_of_players+1].split(":")
    triangle_length = int(triangle_length_line[1])

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

    for j in range(len(lines)-1, index_of_scores, -1):
        if ("These are the moves:" == lines[j]):
            moves_lines = lines[j:]
            if "" in moves_lines:
                last_line_of_moves = moves_lines.index("")
                moves_lines = moves_lines[1:last_line_of_moves]
            break
    
    return get_game_settings_from_log(scores_lines, moves_lines, players_list, triangle_length)


def get_players_list_from_log(lines: List[str]) -> list[Player]:
    players_list = []
    for index in range(0, len(lines), 5):
        players_list.append(Player(lines[index],
                                   COLORS[lines[index+1]],
                                   TRIANGLES[lines[index+3]],
                                   lines[index+2] == "True"))
    return players_list


def get_game_settings_from_log(scores_lines: List[str], moves_lines: List[str], players_list: List[Player], triangle_length: int = 4) -> Tuple[GameSettings,bool]:
    game_settings = GameSettings()
    game_settings.players_list = players_list
    game_settings.init_only_board(triangle_length)
    game_settings.score_board.init_players_scores(game_settings.players_list)
    set_scores_board_from_log(scores_lines, game_settings)
    
    if(moves_lines==[]):
        return (game_settings,True)
    print(moves_lines)
    set_moves_and_move_from_log(moves_lines[1:], game_settings)
    return (game_settings,False)


def set_moves_and_move_from_log(moves_lines: List[str], game_settings: GameSettings) -> None:
    players_list = game_settings.players_list
    for line in moves_lines:
        splited_line = line.split("_")
        for i in range(len(players_list)):
            if players_list[i].name == splited_line[1]:
                player_to_move = players_list[i]
        current_loc = from_str_to_coordinates(splited_line[2])
        go_to = from_str_to_coordinates(splited_line[3])
        moveValidation.move_player(
            game_settings, player_to_move, current_loc, go_to)


def set_scores_board_from_log(scores_lines: List[str], game_settings: GameSettings) -> None:
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


