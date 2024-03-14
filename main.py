from Board import Board
from BoardValues import BoardValues
from moveValidation import MoveValidation
from setting_for_game import GameSettings
import triangles_funcs


def is_end_game(self) -> bool:
    pass


def play(self) -> None:
    # """
    # The main driver of the Game. Manages the game until completion.
    # :return: None
    # """
    # end_game = False
    # while (not end_game):
    #     if (not self.__single_turn()):
    #         print("game ended")
    #         end_game = True
    #     if (self.__is_end_game()):
    #         print("game ended")
    #         end_game = True
    pass


def main():
    print("Welcome to Chinese Checkers Game!")
    board = Board()
    game_settings = GameSettings()
    # game_settings.board.fill_upper_triangle(BoardValues.RED)
    game_settings.init_board()
    # game_settings.board.print_board()
    # print(game_settings.board.is_on_board((6,8)))
    move = MoveValidation(game_settings)
    print(move.get_set_of_possible_jumps((6,10),{}))

if __name__ == "__main__":
    main()
