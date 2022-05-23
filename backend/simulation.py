from  teams_dict import teams
import random

class Game:
    def __init__(self, Team1, Team2):
        self.T1 = Team1
        self.T2 = Team2
        self.result = random.randint(1,100)
        print(f"-----   We have a matchup between teams: {self.T1.city} and {self.T2.city}   -----")
        self.T1Prob = (Team1.strength / (Team1.strength + Team2.strength)) * 100
        print(f"Chance of {self.T1.ab} winning: {round(self.T1Prob)}%")
        print(f"Chance of {self.T2.ab} winning: {round((100-self.T1Prob))}%")

        if self.result < self.T1Prob:
            self.winner = self.T1.ab
        else:
            self.winner = self.T2.ab

        print(f"The winner is {teams[self.winner]['city']}.")


class Team:
    def __init__(self, team, strength):
        self.ab = team
        self.city = teams[team]['city']
        self.division = teams[team]['division']
        self.strength = strength

def main():
    t1 = Team('TOR', 20)
    t2 = Team('BOS', 20)

    game = Game(t1, t2)

main()
