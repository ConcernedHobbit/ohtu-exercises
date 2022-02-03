from typing import List
from player_reader import PlayerReader
from player import Player

class PlayerStats:
  def __init__(self, reader: PlayerReader):
    self.reader = reader

  def top_scorers_by_nationality(self, nationality: str) -> List[Player]:
    return filter(
      lambda player: player.nationality == nationality, 
      self.reader.get_players()
    )