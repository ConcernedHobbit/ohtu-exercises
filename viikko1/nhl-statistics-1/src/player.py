class Player:
    def __init__(self, name: str, team: str, goals: int, assists: int):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    @property
    def points(self) -> int:
        return self.goals + self.assists

    def __str__(self) -> str:
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"
