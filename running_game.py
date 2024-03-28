from typing import Tuple
from datetime import datetime
import re
from typing import Tuple, Union
from logger import Logger
from player import Player
from game_settings import GameSettings
import moveValidation
import checking_dest
import player_instruments_pos
import input_provider
import random
import read_logger

Coordinates = Tuple[int, int]


def create_new_game_settings(game_settings: GameSettings) -> Tuple[GameSettings, bool]:
    """
    Ask the user if to start a new game or to load an existing one.
    Creates game settings based on user input.

    Args:
        game_settings (GameSettings): The current game settings.

    Returns:
        Tuple[GameSettings, bool]: A tuple containing the updated game settings and a boolean value indicating whether it is the first game in the log file.
    """
    is_new_game = input_provider.make_yes_no_dialog("Welcome to Chinese Checkers Game!",
                                                    "Do you want to load a game or to start a new one?",
                                                    "start a new game", "load a game")
    if is_new_game:
        file_name = player_pick_valid_file_name(game_settings)
        game_settings.init_board()
        another_game = True
        Logger.create_file(file_name, game_settings.players_list,
                           game_settings.board.triangle_length)
    else:
        file_name = get_existing_file_name(game_settings)
        game_settings, another_game = read_logger.read_and_load_log_file(
            file_name)
    return (game_settings, another_game)


def get_existing_file_name(game_settings: GameSettings) -> str:
    """
    Prompts the user to enter the name of an existing game file to load.

    Args:
        game_settings (GameSettings): The current game settings.

    Returns:
        str: The name of the existing game file to load.
    """
    while (True):
        file_name = input_provider.get_input_dialog(
            "Enter the name of the game you want to load: ", cancel_text1="Back")
        if (file_name == None):
            create_new_game_settings(game_settings)
        if (file_name[-4:] != ".txt"):
            file_name = file_name+".txt"
        try:
            with open(file_name, 'r') as f:
                # if(f.name==file_name):
                break
        except FileNotFoundError:
            input_provider.print_message_dialog(
                "The file does not exist, please try again.", "Ok")
    Logger.name = file_name
    return file_name


def player_pick_valid_file_name(game_settings: GameSettings) -> str:
    """
    Prompts the player to enter a valid file name for the tournament file.

    Args:
        game_settings (GameSettings): The game settings object.

    Returns:
        str: The valid file name entered by the player.
    """
    while (True):
        file_name = input_provider.get_input_dialog(
            "Pick a name to the tournament file: ", cancel_text1="Back")
        if (file_name == None):
            create_new_game_settings(game_settings)
        results = re.search("^(?!^ $)[a-zA-Z0-9_ -]+$", file_name)
        if (results == None):
            input_provider.print_message_dialog(
                "The name cannot be empty and cannot include symbols as !@#$%^&* etx. please try again.", "Ok")
        else:
            break
    return file_name


def is_winner(game_settings: GameSettings, player: Player):
    """
    Check if the player is the winner of the game.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player to check.

    Returns:
        bool: True if the player is the winner, False otherwise.
    """
    if (checking_dest.is_p1_win_in_dest(game_settings, player)):
        return True
    return False


def player_choose_piece_to_move(game_settings: GameSettings, player: Player) -> Coordinates:
    """
    Prompts the player to choose a piece to move on the game board.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player who is choosing the piece to move.

    Returns:
        Coordinates: The coordinates of the chosen piece on the game board.
    """
    player_locs_list = player_instruments_pos.get_all_locs_4player(
        game_settings.board.the_board, player)
    pieces_nums = game_settings.board.pieces_nums
    while (True):
        while (True):
            piece = input_provider.get_input_with_autocomplete(
                "What piece would you like to move? Click Tab key to see the options and choose from them.",
                pieces_nums)

            if (piece in pieces_nums):
                break

            print("Invalid input, let's try again.")

        index_in_players_locs = pieces_nums.index(piece)
        current_loc = player_locs_list[index_in_players_locs]
        if (moveValidation.get_all_possible_moves(game_settings, current_loc) != []):
            break
        print("This piece has no place to move, please choose another one.")

    return current_loc


def player_choose_destination(game_settings: GameSettings, player: Player, current_loc: Coordinates) -> Coordinates:
    """
    Allows the player to choose a destination to move to.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player object.
        current_loc (Coordinates): The current location of the player.

    Returns:
        Coordinates: The coordinates of the chosen destination.
    """
    all_possible_moves = moveValidation.get_all_possible_moves(
        game_settings, current_loc)
    emoji_possible_moves = game_settings.board.create_emoji_moves(
        len(all_possible_moves))

    while (True):
        emojy_to_go = input_provider.get_input_with_autocomplete(
            "Where would you like to move it? Click Tab key to see the options. ",
            emoji_possible_moves)

        if (emojy_to_go in emoji_possible_moves):
            break

        print("Invalid input. Let's try again.")

    index_in_possible_moves = emoji_possible_moves.index(emojy_to_go)
    go_to = all_possible_moves[index_in_possible_moves]
    return go_to


def single_comp_turn(game_settings: GameSettings, comp_player: Player) -> Tuple[Coordinates, Coordinates]:
    """
    Executes a single turn for the computer player.

    Args:
        game_settings (GameSettings): The settings of the game.
        comp_player (Player): The computer player.

    Returns:
        Tuple[Coordinates, Coordinates]: A tuple containing the current location and the destination location of the computer player's move.
    """
    while (True):
        current_loc = random.choice(player_instruments_pos.get_all_locs_4player(
            game_settings.board.the_board, comp_player))

        if (moveValidation.is_valid_current_loc(game_settings, comp_player, current_loc)):
            break

    while (True):
        go_to = random.choice(
            moveValidation.get_all_possible_moves(game_settings, current_loc))

        if (moveValidation.is_valid_move(game_settings, comp_player, current_loc, go_to)):
            break

    moveValidation.move_player(game_settings, comp_player, current_loc, go_to)
    return (current_loc, go_to)


def single_player_turn(game_settings: GameSettings, player: Player) -> Tuple[Coordinates, Coordinates]:
    """
    Executes a single turn for a single player in the game.

    Args:
        game_settings (GameSettings): The settings of the game.
        player (Player): The player whose turn it is.

    Returns:
        Tuple[Coordinates, Coordinates]: A tuple containing the current location and the destination coordinates of the player's move.
    """
    game_settings.board.clear_screen()
    game_settings.board.print_board(player)
    while (True):
        current_loc = player_choose_piece_to_move(game_settings, player)
        if (moveValidation.is_valid_current_loc(game_settings, player, current_loc)):
            break
        print("Invalid input, let's try again.")
    game_settings.board.clear_screen()
    game_settings.board.print_board(None,
                                    moveValidation.get_all_possible_moves(game_settings, current_loc), current_loc)
    while (True):
        go_to = player_choose_destination(game_settings, player, current_loc)
        if (moveValidation.is_valid_move(game_settings, player, current_loc, go_to)):
            break
        print("Invalid input, let's try again.")
    moveValidation.move_player(game_settings, player, current_loc, go_to)
    game_settings.board.clear_screen()
    game_settings.board.print_board()
    return (current_loc, go_to)


def single_round(game_settings: GameSettings) -> Union[Player, None]:
    """
    Executes a single round of the game for each player in the game_settings.players_list.

    Args:
        game_settings (GameSettings): The settings for the game.

    Returns:
        Union[Player, None]: The winning player if there is one, otherwise None.
    """
    for player in game_settings.players_list:
        if player.is_comp:
            current_loc, go_to = single_comp_turn(game_settings, player)
        else:
            current_loc, go_to = single_player_turn(game_settings, player)
        Logger.add_message(player.name, current_loc, go_to)
        if is_winner(game_settings, player):
            return player
    return None


def play(game_settings: GameSettings) -> None:
    """
    Plays the game using the provided game settings.
    The driver function of the game.

    Args:
        game_settings (GameSettings): The settings for the game.

    Returns:
        None
    """

    introduction = """Before we begin: \n
    In the next window you will see the board.\n
    Each turn the pieces of the relevant player are marked as numbers and
    the player needs to choose which piece he wants to move. \n
    After that, emojies will appear on the board. \n
    🎯 - represents the piece that the player chose to move.\n
    Animal emojies represent the places that the player can move the piece to.\n
    Enjoy and Good luck!"""
    input_provider.print_message_dialog(introduction, "Lets go!")

    input_provider.print_message_dialog(
        f"{game_settings.players_list[0].name}, you go first!", "lets go!")
    end_game = False
    while (not end_game):
        player = single_round(game_settings)
        if (player != None):
            end_game = True

    game_settings.score_board.add_winner(player)
    for p in game_settings.players_list:
        if p != player:
            game_settings.score_board.add_loser(p)
    time = datetime.now().strftime("%Y-%m-%d")+" " + \
        datetime.now().strftime("%H:%M:%S")
    Logger.add_scores_message("The game ended. These are the results: " +
                              "\n"+time+" "+game_settings.score_board.get_str_scores())
    input_provider.print_message_dialog(
        game_settings.score_board.get_str_scores()+f"\nGood job everyone, the game ended.", "Game Ended!")
    game_settings.board.print_board()
