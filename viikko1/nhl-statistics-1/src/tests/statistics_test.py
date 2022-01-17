import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )


    def test_search_loytaa_pelaajan(self):
        semeiko = self.statistics.search("Semenko")
        s = f"{semeiko}"
        self.assertEqual(s,"Semenko EDM 4 + 12 = 16")


    def test_search_palauttaa_None_jos_pelaajaa_ei_loydy(self):

        self.assertIsNone(self.statistics.search("joku"))

    def test_team_paluttaa_oikean_joukkoeen(self):
        team = self.statistics.team("PIT")
        team_list = []
        for t in team:
            team_list.append(f"{t}")

        self.assertEqual(team_list,["Lemieux PIT 45 + 54 = 99"])

    def test_top_scorers_paluttaa_oikeat_pelaajat(self):
        best = self.statistics.top_scorers(0)
        best_list = []
        for t in best:
            best_list.append(f"{t}")

        self.assertEqual(best_list,["Gretzky EDM 35 + 89 = 124"])
    '''
    assertIsNone()
    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top_scorers(self, how_many):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
        '''