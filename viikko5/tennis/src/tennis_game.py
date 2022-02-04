from dataclasses import dataclass
from typing import Optional


SCORE_NAMES = [
    "Love",
    "Fifteen",
    "Thirty",
    "Forty"
]

@dataclass
class Player:
    name: str
    score: int = 0

    def __str__(self):
        return f"{self.name} {SCORE_NAMES[self.score]}"

    def won_point(self):
        self.score += 1

    @property
    def in_endgame(self):
        return self.score >= 4

class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.players = [
            Player(player1_name),
            Player(player2_name)
        ]

    def player_by_name(self, player_name: str) -> Optional[Player]:
        return next(
            filter(
                lambda player: player.name == player_name,
                self.players
            ),
            None
        )

    def _score_name(self, player_number: int) -> Optional[str]:
        if 0 > player_number > len(self.players):
            return None

        score = self.players[player_number].score

        if score > len(SCORE_NAMES):
            return None

        return SCORE_NAMES[score]

    def won_point(self, player_name: str) -> bool:
        player = self.player_by_name(player_name)

        if not player:
            return False

        player.won_point()
        return True

    @property
    def difference(self) -> int:
        return self.players[0].score - self.players[1].score

    @property
    def is_endgame(self) -> bool:
        return self.players[0].in_endgame or self.players[1].in_endgame

    @property
    def winner(self) -> Optional[Player]:
        if self.players[0].in_endgame and self.difference > 1:
            return self.players[0]

        elif self.players[1].in_endgame and self.difference < -1:
            return self.players[1]

        return None

    def get_score(self) -> str:
        if self.difference == 0:
            if self.players[0].in_endgame:
                return "Deuce"

            return f"{self._score_name(0)}-All"

        if self.is_endgame:
            if self.difference == 1:
                return f"Advantage {self.players[0].name}"

            if self.difference == -1:
                return f"Advantage {self.players[1].name}"

            return f"Win for {self.winner.name}"

        return f"{self._score_name(0)}-{self._score_name(1)}"