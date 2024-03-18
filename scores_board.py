from typing import Tuple, List, Dict

from player import Player

class ScoresBoard:
    """
    
    """
    def __init__(self) -> None:
        self.scores_board={}
    def init_players(self,players_list:List[Player])->None:
        for player in players_list:
            self.scores_board[player.name]=[0,0]

    def add_winner(self,player:Player)->None:
        self.scores_board[player.name][0]+=1

    def add_loser(self,player:Player)->None:
        self.scores_board[player.name][1]+=1
        
    def get_str_scores(self)->None:
        str_scores=""
        highest_wins = max(self.scores_board.values(), key=lambda x: x[1])
        for key, value in self.scores_board.items():
            if value == highest_wins:
                the_big_winner = key
                break
        str_scores+=the_big_winner+", you won!\nThe other players scores are:\n"
        for player in self.scores_board.keys():
            # str_scores+=str(player.name) + " won: " + str(self.scores_board[player][0])+ " times and lost: " + str(self.scores_board[player][1])
            str_scores+=f"{player} won: " + str(self.scores_board[player][0])+ " times and lost: " + str(self.scores_board[player][1])
        
        return str_scores
        