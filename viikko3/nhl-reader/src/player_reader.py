import requests
from typing import List
from player import Player

class PlayerReader:
  def __init__(self, url: str):
    self.url = url
  
  def get_players(self) -> List[Player]:
    res = requests.get(self.url).json()
    
    players = []
    for player_dict in res:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            int(player_dict['assists']),
            int(player_dict['goals']),
            int(player_dict['penalties']),
            player_dict['team'],
            int(player_dict['games'])
        )
        players.append(player)

    return players