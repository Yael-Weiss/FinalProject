from typing import Tuple, Union
from board import EMOJI_NUMS, EMOJI_POSSIBLE_MOVES, Board
from player import Player
from setting_for_game import GameSettings
import moveValidation
import checking_dest
import triangles_funcs
import input_provider

Coordinates = Tuple[int, int]


def is_end_game(player: Player,) -> bool:
    pass


def is_winner(game_settings: GameSettings, player: Player):
    # needs to add case that there are stuck pieces inside
    if (checking_dest.is_all_in_dest(game_settings.board, player)):
        return True
    return False


def is_valid_current_loc(board: Board, player: Player, current_loc: Coordinates) -> bool:
    return board.cell_content(current_loc) == player.color

def single_round(game_settings: GameSettings) -> Union[Player, None]:
    for player in game_settings.players_list:
        single_player_turn(game_settings, player)
        if (is_winner(game_settings, player)):
            return player
    return None

def player_choose_piece_to_move(game_settings: GameSettings, player: Player) -> Coordinates:
    player_locs_list = triangles_funcs.get_all_locs_4player(
        game_settings.board.the_board, player)
    print(player_locs_list)
    emojy_nums = EMOJI_NUMS
    while (True):
        emojy = input_provider.get_input_with_autocomplete(
            "What piece would you like to move? Click Tab key to see the options.",
            emojy_nums)
        if(emojy in emojy_nums):
            break
        else:
            print("Invalid input, let's try again.")
    index_in_players_locs = emojy_nums.index(emojy)
    current_loc=player_locs_list[index_in_players_locs]
    return current_loc


def player_choose_destination(game_settings: GameSettings, player: Player, current_loc: Coordinates) -> Coordinates:
    # possible_moves = moveValidation.get_list_of_possible_moves(
    #     game_settings, current_loc)
    # possible_jumps = list(moveValidation.get_set_of_possible_jumps(
    #     game_settings, current_loc, set({})))
    all_possible_moves = moveValidation.get_all_possible_moves(game_settings,player,current_loc)
    emoji_possible_moves = EMOJI_POSSIBLE_MOVES
    # while(True):
    #     go_to=input("Where would you like to move it? ", end="\n")
    #     if(moveValidation.is_valid_move(game_settings,player,current_loc,go_to)):
    #         break
    #     print("Invalid choice. Let's try again.")


def single_player_turn(game_settings: GameSettings, player: Player) -> None:
    pass

    moveValidation.move_player(
        game_settings, player, current_loc, (4, 10))  # go_to)


def play(game_settings: GameSettings) -> None:
    # """
    # The main driver of the Game. Manages the game until completion.
    # :return: None
    # """
    end_game = False
    while (not end_game):
        we_have_winner = single_round(game_settings)
        if (we_have_winner):
            print(f"the winner is....{we_have_winner.name}! ")
            print("good job everyone, the game ended")
            end_game = True


if __name__ == "__main__":
    pass
