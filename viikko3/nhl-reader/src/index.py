import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    res = requests.get(url).json()
    
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

    finnish_players = filter(lambda player: player.nationality == 'FIN', players)
    print(*finnish_players, sep='\n')

if __name__ == "__main__":
    main()
