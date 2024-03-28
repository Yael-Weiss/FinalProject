from typing import Tuple
from logger import Logger
from game_settings import GameSettings
import running_game
import input_provider

Coordinates = Tuple[int, int]
DIRECTIONS_LIST = [(-2, -2), (-2, 2), (2, -2), (2, 2)]


def main():
    game_settings = GameSettings()
    another_game = False
    while (True):
        game_settings,another_game = running_game.create_new_game_settings(
            game_settings)
        # game_settings.players_list[0].destination_tri = Triangles.upper_tri
        while (True):
            Logger.start_new_game_log(another_game)
            running_game.play(game_settings)
            another_game = input_provider.make_yes_no_dialog(
                "Chinese Checkers Game", "Do you want to play again?")
            if not another_game:
                break
            game_settings.init_only_board(game_settings.board.triangle_length)
        break


if __name__ == "__main__":
    main()


