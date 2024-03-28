from typing import List, Tuple
from datetime import datetime

from player import Player
from triangles import Triangles

Coordinates = Tuple[int, int]


class Logger:
    def intro_4_new_game(file_name: str, players_list: List[Player],triangle_length:int) -> None:
        time = datetime.now().strftime("%Y-%m-%d")+" " + \
            datetime.now().strftime("%H:%M:%S")
        with open(Logger.name, 'w') as f:
            f.write(
                time+f" Game log - These are the players:\n")
            for player in players_list:
                f.write(player.name+"\n"+str(player.color)+"\n"+str(player.is_comp) +
                        "\n"+str(player.starting_tri)+"\n"+str(player.destination_tri)+"\n")
            f.write("\nTriangleLength:"+str(triangle_length)+"\n")
            
            

    def create_file(file_name: str, players_list: List[Player], triangle_length:int=4) -> None:
        Logger.name = file_name+".txt"
        Logger.intro_4_new_game(file_name, players_list, triangle_length)

    def start_new_game_log() -> None:
        with open(Logger.name, 'a') as f:
            f.write("\nThese are the moves:\n")

    def add_message(player_name: str, current_loc: Coordinates, go_to: Coordinates) -> None:
        time = datetime.now().strftime("%Y-%m-%d")+" " + \
            datetime.now().strftime("%H:%M:%S")
        message = time+f"_{player_name}_{current_loc}_{go_to}"
        with open(Logger.name, 'a') as f:
            f.write(message + '\n')

    def add_scores_message(message: str) -> None:
        with open(Logger.name, 'a') as f:
            f.write("\n"+message + '\n\n')

