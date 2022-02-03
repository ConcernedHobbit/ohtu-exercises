from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    finnish_players = stats.top_scorers_by_nationality('FIN')
    print(*finnish_players, sep='\n')

if __name__ == "__main__":
    main()
