from typing import List, Tuple
from datetime import datetime

from player import Player
from triangles import Triangles


Coordinates = Tuple[int, int]
class Logger:
    def create_file(file_name: str,players_list:List[Player]) -> None:
        Logger.name = file_name
        time=datetime.now().strftime("%Y-%m-%d")+" "+datetime.now().strftime("%H:%M:%S")
        with open(Logger.name, 'w') as f:
            f.write(time+" Game log - These are the players:\n")
            for player in players_list:
                f.write(player.name+"\n"+str(player.color)+"\n"+str(player.is_comp)+"\n"+str(player.starting_tri)+"\n"+str(player.destination_tri)+"\n\n")

    def add_message(player_name:str,current_loc:Coordinates,go_to:Coordinates)->None:
        time=datetime.now().strftime("%Y-%m-%d")+" "+datetime.now().strftime("%H:%M:%S")
        message = time+f",{player_name},{current_loc},{go_to}"
        with open(Logger.name, 'a') as f:
            f.write(message + '\n')
        
p1=Player("shir","red",Triangles.upper_tri)
Logger.create_file("log10.txt",[p1])
Logger.add_message(p1.name,(1,1),(2,2))
