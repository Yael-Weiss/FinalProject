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
print(type(BoardValues.BLUE.name))
# colors_dic.pop(str(BoardValues.RED))
# print(colors_dic)




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
