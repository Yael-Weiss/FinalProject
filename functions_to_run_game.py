from typing import Tuple
from Board import Board
from player import Player
from setting_for_game import GameSettings
import moveValidation

Coordinates = Tuple[int, int]

def is_end_game(player:Player,) -> bool:
    pass
def is_valid_current_loc(board:Board,player:Player,current_loc:Coordinates)->bool:
    return board.cell_content(current_loc)==player.color

def single_round():
    pass

def single_turn(player:Player,game_settings:GameSettings)->None:
    while(True):
        current_loc=input("What piece would like to move? ")
        if(is_valid_current_loc(current_loc)):
            break
        print("Invalid choice. Let's try again. ")
    while(True):
        go_to=input("Where would you like to move it? ", end="\n")
        if(moveValidation.is_valid_move(game_settings,player,current_loc,go_to)):
            break
        print("Invalid choice. Let's try again.")
def play(self) -> None:
    # """
    # The main driver of the Game. Manages the game until completion.
    # :return: None
    # """
    end_game = False
    # while (not end_game):
    #     if (not self.__single_turn()):
    #         print("game ended")
    #         end_game = True
    #     if (self.__is_end_game()):
    #         print("game ended")
    #         end_game = True
    pass

