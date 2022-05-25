from  teams_dict import teams
import pandas as pd
import random

class Game:
    def __init__(self, Team1, Team2):
        self.T1 = Team1
        self.T2 = Team2
        self.result = random.randint(1,100)
        print(f"-----   We have a matchup between teams: {self.T1.city} and {self.T2.city}   -----")
        self.T1Prob = (Team1.strength / (Team1.strength + Team2.strength)) * 100
        # print(f"Chance of {self.T1.ab} winning: {round(self.T1Prob)}%")
        # print(f"Chance of {self.T2.ab} winning: {round((100-self.T1Prob))}%")

        self.handle_result()

    def handle_result(self):
        # Team 1 wins in regulation
        if self.result < self.T1Prob:
            self.T1.update_record("W")
            self.T2.update_record("L")
            print(f"The winner is the {self.T1.name}.")
        # Team 2 wins in regulation
        else:
            self.T1.update_record("L")
            self.T2.update_record("W")
            print(f"The winner is the {self.T2.name}.")
        
        


class Team:
    def __init__(self, team, strength):
        self.ab = team
        self.city = teams[team]['city']
        self.division = teams[team]['division']
        self.name = teams[team]['name']
        self.GP = 0
        self.W = 0
        self.L = 0
        self.OTL = 0
        self.P = 0
        self.strength = strength
    
    def update_record(self, result):
        print("It happened")
        if result == 'W':
            self.W += 1
        elif result == 'L':
            self.L += 1
        elif result == 'OTL':
            self.OTL += 1
        
        self.GP = self.W + self.L + self.OTL
        self.P = self.W * 2 + self.OTL
            


class Season:
    def __init__(self, year):
        self.year = year
        self.get_season_data()
        self.create_teams()
        self.create_standings()

    def get_season_data(self):
        # Parse the CSV
        self.schedule = pd.read_csv(f'data/schedules/{self.year}.csv')

        # Setting column names
        col_names = ['Date', 'Away', 'Home']
        self.schedule.columns = col_names

        # Convert full names to abbreviations
        translation = {}
        team_abb_list = list(teams)
        for team in team_abb_list:
            translation[(teams[team]['name'])] = team
        
        self.schedule = self.schedule.replace({'Home': translation})
        self.schedule = self.schedule.replace({'Away': translation})

    def create_teams(self):
        self.active_teams = {}
        for team in teams:
            self.active_teams[team] = (Team(team, 100))

    def create_standings(self):
        self.standings = pd.DataFrame()
        
            
        
        
        

def main():
    # t1 = Team('TOR', 20)
    # t2 = Team('BOS', 20)

    year = Season(2022)
    #for value in year.active_teams.items():
        #print(value['name'])
        #if t.division == 'Atlantic':
         #   print(t.name)
    
    #print(year.active_teams['TOR'].name)
    g = Game(year.active_teams['TOR'], year.active_teams['BOS'])
    #print(year.active_teams)
    # for key, team in year.active_teams.items():
    #     #print(value.city)
    #     print(f"{team.ab}: {team.P} points.")

main()
