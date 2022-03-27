

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {
            player1_name: 0,
            player2_name: 0,
        }


    def won_point(self, player_name):
        self.players[player_name] +=1


    def get_score(self):
        score = ""
        results = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"

        }
        score = list(self.players.values())
        player1_points = score[0]
        player2_points = score[1]

        if player1_points == player2_points:
            if player1_points <= 3:
                return results[player1_points] + "-All"
            else:
                return "Deuce"
        if player1_points <= 3 and player2_points <= 3:
            score = results[player1_points] + "-" + results[player2_points]

        if player1_points > player2_points and player2_points >= 3:
            score = "Advantage player1"

        if player2_points > player1_points and player1_points >= 3:
            score = "Advantage player2"


        if player1_points >= 4 and player2_points >= 0 and player1_points - player2_points >= 2:
            score = "Win for player1"

        if player2_points >= 4 and player1_points >= 0 and (player2_points - player1_points) >= 2:
            score = "Win for player2"

        return score



