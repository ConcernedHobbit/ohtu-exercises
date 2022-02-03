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
    
    def __str__(self):
        return f"[{self.team}] [{self.nationality}] {self.name}: {self.goals} goals, {self.assists} assists"
