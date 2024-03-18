from typing import List
from BoardValues import BoardValues
from logger import Logger
from player import Player
from setting_for_game import GameSettings
from triangles import Triangles
import moveValidation

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


def from_str_to_coordinates(str: str):  # -> tuple[int,int]:
    coma_index = str.find(",")
    num1 = str[1:coma_index]
    num2 = str[coma_index+1:len(str)-1]
    return (int(num1), int(num2))

def read_and_load_log_file(file_name: str)->GameSettings:
    with open(file_name, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    index = lines.index("")
    lines_for_players_list = lines[1:index]
    lines_for_game_settings = lines[index+2:]
    players_list = get_players_list_from_log(lines_for_players_list)
    return get_game_settings_from_log(lines_for_game_settings, players_list)


def get_players_list_from_log(lines: List[str]) -> list[Player]:
    players_list = []
    for index in range(0, len(lines), 5):
        players_list.append(Player(lines[index],
                                   COLORS[lines[index+1]],
                                   TRIANGLES[lines[index+3]],
                                   lines[index+2] == "True"))
    return players_list


def get_game_settings_from_log(lines: List[str], players_list: List[Player]) -> GameSettings:

    game_settings = GameSettings()
    game_settings.players_list = players_list
    game_settings.init_only_board()
    for line in lines:
        splited_line = line.split("_")
        for i in range(len(players_list)):
            if players_list[i].name == splited_line[1]:
                player_to_move = players_list[i]
        current_loc = from_str_to_coordinates(splited_line[2])
        go_to = from_str_to_coordinates(splited_line[3])
        moveValidation.move_player(
            game_settings, player_to_move, current_loc, go_to)
    return game_settings


#players_list = get_players_list_from_log("Trol.txt")
# game = read_and_load_log_file("ARiel.txt")
# game.board.print_board()
# print(game.players_list[0].name)


# print(content[start_players+1])
# get_game_settings_from_log("Trol.txt")
