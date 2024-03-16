from BoardValues import BoardValues


colors_dic= {BoardValues.RED.name: BoardValues.RED.value,
                 BoardValues.BLUE.name: BoardValues.BLUE.value,
                 BoardValues.YELLOW.name: BoardValues.YELLOW.value,
                 BoardValues.PURPLE.name: BoardValues.PURPLE.value,
                 BoardValues.GREEN.name: BoardValues.GREEN.value,
                 BoardValues.ORANGE.name: BoardValues.ORANGE.value}
# print("Welcome to chinese checkers game!")
# # num_of_players=input("How many players would like to play? ")
# colors_str=', '.join(colors_dic.keys())
# # name_player1=input("What is the name of the first player? ")
# color_player1=input(f"What color would you like to be? please choose one of the options: {colors_str}")
# print(type(BoardValues.BLUE.name))
# colors_dic.pop(str(BoardValues.RED))
# print(colors_dic)
# ANSI escape codes for changing the background color
BACKGROUND_YELLOW = '\033[43m'
BACKGROUND_RESET = '\033[0m'

# Print text with yellow background
print(BACKGROUND_YELLOW + "This text has a yellow background." + BACKGROUND_RESET)




# def get_set_of_possible_jumps(game_settings:GameSettings, location:Coordinates, possible_jumps_set: set[Coordinates]) -> set[Coordinates]:

#     if not (game_settings.board.is_on_board(location)):
#         return possible_jumps_set
#     row, col = location
#     DIRECTIONS_LIST=[(-2,-2),(-2,2),(2,-2),(2,2),(0,2),(0,-2)]
#     if (game_settings.board.is_on_board((row-2, col-2))):
#         # if(game_settings.board.the_board[row-2][col-2] != BoardValues.EMPTY
#         #    and game_settings.board.the_board[row-2][col-2] != BoardValues.OUT_OF_BOARD):
#         if (game_settings.board.the_board[row-2][col-2] == BoardValues.EMPTY and (row-2, col-2) not in possible_jumps_set):
#             possible_jumps_set.add((row-2, col-2))
#             get_set_of_possible_jumps((row-2, col-2), possible_jumps_set)

#     if (game_settings.board.is_on_board((row-2, col+2))):
#         if (game_settings.board.the_board[row-2][col+2] == BoardValues.EMPTY and (row-2, col+2) not in possible_jumps_set):
#             possible_jumps_set.add((row-2, col+2))
#             get_set_of_possible_jumps((row-2, col+2), possible_jumps_set)
#     if (game_settings.board.is_on_board((row+2, col-2))):
#         if (game_settings.board.the_board[row+2][col-2] == BoardValues.EMPTY and (row+2, col-2) not in possible_jumps_set):
#             possible_jumps_set.add((row+2, col-2))
#             get_set_of_possible_jumps((row+2, col-2), possible_jumps_set)

#     if (game_settings.board.is_on_board((row+2, col+2))):
#         if (game_settings.board.the_board[row+2][col+2] == BoardValues.EMPTY and (row+2, col+2) not in possible_jumps_set):
#             possible_jumps_set.add((row+2, col+2))
#             get_set_of_possible_jumps((row+2, col+2), possible_jumps_set)

#     if (game_settings.board.is_on_board((row, col+2))):
#         if (game_settings.board.the_board[row][col+2] == BoardValues.EMPTY and (row, col+2) not in possible_jumps_set):
#             possible_jumps_set.add((row, col+2))
#             get_set_of_possible_jumps((row, col+2), possible_jumps_set)

#     if (game_settings.board.is_on_board((row, col-2))):
#         if (game_settings.board.the_board[row][col-2] == BoardValues.EMPTY and (row, col-2) not in possible_jumps_set):
#             possible_jumps_set.add((row, col-2))
#             get_set_of_possible_jumps((row, col-2), possible_jumps_set)

#     return possible_jumps_set


# move = MoveValidation(game_settings)
    # # print((4,8) in move.get_list_of_possible_moves((3,9)))
    # # print(move.is_in_triangle_not_des(p1,(4,8)))
    # move.move_player(p1,(3,9),(4,8))
    # game_settings.board.print_board()
    # print(checking_dest.is_all_in_upper_tri_same_color(game_settings.board,p1))
    # print(p1.color)
    # print(move.game_setting.board.cell_content((3,9)))