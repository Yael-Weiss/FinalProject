from typing import Tuple, List, Dict

from player import Player

class ScoresBoard:
    """
    
    """
    def __init__(self,players_list: List[Tuple[Player,int,int]]) -> None:
        self.players_list=players_list
        