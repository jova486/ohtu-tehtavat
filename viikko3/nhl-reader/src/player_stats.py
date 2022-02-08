from player import Player
from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, playerReader):
        self.playerReader = playerReader

    def top_scorers_by_nationality(self, nationality):

        query = self.playerReader.get_players()
        players = []
        for player in query:
            if player.nationality == nationality:
                players.append(player)

        players = sorted(players, key=lambda x: x.total, reverse=True)
        return players

    def __str__(self):
        return f"{self.name:20} {self.team:4} {str(self.goals):>2} + {str(self.assists):>2} = {str(self.total):>2}"
