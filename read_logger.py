from typing import List
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


def from_str_to_coordinates(str: str) -> tuple[int,int]:
    coma_index = str.find(",")
    num1 = str[1:coma_index]
    num2 = str[coma_index+1:len(str)-1]
    return (int(num1), int(num2))

def read_and_load_log_file(file_name: str) -> GameSettings:
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    last_line_of_players = lines.index("")
    lines_for_players_list = lines[1:last_line_of_players]
    players_list = get_players_list_from_log(lines_for_players_list)
    triangle_length_line=lines[last_line_of_players+1].split(":")
    triangle_length = int(triangle_length_line[1])
    for j in range(len(lines)-1, -1, -1):
        if ("These are the moves:" == lines[j]):
            lines = lines[j:]
            break
    if "" not in lines:
        last_line_of_moves = len(lines)
    else:
        last_line_of_moves=lines.index("")
    lines_for_game_settings = lines[1:last_line_of_moves]
    rest_of_lines = lines[last_line_of_moves+1:]
    print(lines_for_game_settings)
    print("p")
    print(rest_of_lines)
    return get_game_settings_from_log(rest_of_lines,lines_for_game_settings, players_list,triangle_length)


def get_players_list_from_log(lines: List[str]) -> list[Player]:
    players_list = []
    for index in range(0, len(lines), 5):
        players_list.append(Player(lines[index],
                                   COLORS[lines[index+1]],
                                   TRIANGLES[lines[index+3]],
                                   lines[index+2] == "True"))
    return players_list


def get_game_settings_from_log(rest_of_lines:List[str],lines: List[str], players_list: List[Player],triangle_length:int=4) -> GameSettings:
    game_settings = GameSettings()
    game_settings.players_list = players_list
    game_settings.init_only_board(triangle_length)
    for line in lines:
        splited_line = line.split("_")
        for i in range(len(players_list)):
            if players_list[i].name == splited_line[1]:
                player_to_move = players_list[i]
        current_loc = from_str_to_coordinates(splited_line[2])
        go_to = from_str_to_coordinates(splited_line[3])
        moveValidation.move_player(
            game_settings, player_to_move, current_loc, go_to)
    
    game_settings.score_board.init_players_scores(game_settings.players_list)

    for line in rest_of_lines:
        if (line == "The other players scores are:"):
            scores_lines=rest_of_lines[rest_of_lines.index(line)+1:]
            break
    print(scores_lines)
    for line in scores_lines:
        splited_line = line.split(" ")
        for i in range(len(players_list)):
            if players_list[i].name == splited_line[0]:
                player_name=players_list[i].name
                game_settings.score_board.set_num_of_wins(player_name,int(splited_line[2]))
                game_settings.score_board.set_num_of_loses(player_name,int(splited_line[6]))
    print(game_settings.score_board.get_str_scores())
            

    return game_settings



