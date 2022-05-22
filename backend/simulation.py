from  teams_dict import teams
class Game:
    def __init__(self, Team1, Team2):
        self.T1 = Team1
        self.T2 = Team2
        print(f"We have a matchup between teams: {self.T1.city} and {self.T2.city}")


class Team:
    def __init__(self, team):
        self.city = teams[team]['city']
        self.division = teams[team]['division']
        print(f"Created an instance of {self.city}")


def main():
    t1 = Team('TOR')
    t2 = Team('BOS')
    game = Game(t1, t2)



main()