class Player:
    def __init__(
        self, 
        name: str, 
        nationality: str, 
        assists: int, 
        goals: int, 
        penalties: int, 
        team: str, 
        games: int
    ):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.team}   {self.name:20}  {self.goals!s:>3} + {self.assists!s:>3} = {self.points!s:>3}"
