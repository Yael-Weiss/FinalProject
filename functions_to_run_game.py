from typing import Tuple, Union
from board import EMOJI_NUMS, EMOJI_POSSIBLE_MOVES, Board
from player import Player
from setting_for_game import GameSettings
import moveValidation
import checking_dest
import triangles_funcs
import input_provider

Coordinates = Tuple[int, int]


def is_end_game(game_settings: GameSettings, player: Player) -> bool:
    pass


def is_winner(game_settings: GameSettings, player: Player):
    # needs to add case that there are stuck pieces inside
    if (checking_dest.is_all_in_dest(game_settings.board, player)):
        return True
    return False


def player_choose_piece_to_move(game_settings: GameSettings, player: Player) -> Coordinates:
    player_locs_list = triangles_funcs.get_all_locs_4player(
        game_settings.board.the_board, player)
    emojy_nums = EMOJI_NUMS
    print(emojy_nums)
    while (True):
        emojy = input_provider.get_input_with_autocomplete(
            "What piece would you like to move? Click Tab key to see the options.",
            emojy_nums)

        if (emojy in emojy_nums):
            break

        print("Invalid input, let's try again.")

    index_in_players_locs = emojy_nums.index(emojy)
    current_loc = player_locs_list[index_in_players_locs]
    return current_loc


def player_choose_destination(game_settings: GameSettings, player: Player, current_loc: Coordinates) -> Coordinates:
    # possible_moves = moveValidation.get_list_of_possible_moves(
    #     game_settings, current_loc)
    # possible_jumps = list(moveValidation.get_set_of_possible_jumps(
    #     game_settings, current_loc, set({})))
    all_possible_moves = moveValidation.get_all_possible_moves(
        game_settings, current_loc)
    emoji_possible_moves = EMOJI_POSSIBLE_MOVES[:len(all_possible_moves)]

    while (True):
        emojy_to_go = input_provider.get_input_with_autocomplete(
            "Where would you like to move it? Click Tab key to see the options. ",
            emoji_possible_moves)
        print(emojy_to_go)
        print(emoji_possible_moves)
        print(emojy_to_go in emoji_possible_moves)
        if (emojy_to_go in emoji_possible_moves):
            break

        print("Invalid input. Let's try again.")

    index_in_possible_moves = emoji_possible_moves.index(emojy_to_go)
    go_to = all_possible_moves[index_in_possible_moves]
    return go_to


def single_player_turn(game_settings: GameSettings, player: Player) -> None:
    game_settings.board.print_board(player)
    while (True):
        current_loc = player_choose_piece_to_move(game_settings, player)
        if (moveValidation.is_valid_current_loc(game_settings, player, current_loc)):
            break
        print("Invalid input, let's try again.")
    game_settings.board.clear_screen()
    game_settings.board.print_board(player,
                                    moveValidation.get_all_possible_moves(game_settings, current_loc))
    while (True):
        go_to = player_choose_destination(game_settings, player, current_loc)
        if (moveValidation.is_valid_move(game_settings, player, current_loc, go_to)):
            break
        print("Invalid input, let's try again.")
    moveValidation.move_player(game_settings, player, current_loc, go_to)
    game_settings.board.clear_screen()
    game_settings.board.print_board()


def single_round(game_settings: GameSettings) -> Union[Player, None]:
    print(game_settings.players_list)
    for player in game_settings.players_list:
        single_player_turn(game_settings, player)
        if (is_winner(game_settings, player)):
            return player
    return None


def play() -> None:
    # """
    # The main driver of the Game. Manages the game until completion.
    # :return: None
    # """
    game_settings = GameSettings()
    game_settings.init_board()
    end_game = False
    while (not end_game):
        player = single_round(game_settings)
        if (player != None):
            end_game = True
    input_provider.print_message_dialog_or_quit(
        f"the winner is....{player.name}! \nGood job everyone, the game ended", "Game Ended!")


if __name__ == "__main__":
    pass
