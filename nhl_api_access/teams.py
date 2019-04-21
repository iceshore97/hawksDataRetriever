import os, requests, json


class Team:

    CURRENT_DB_FIELDS = [
        'CODE',
        'CITY',
        'NAME',
        'MAIN_COLOR',
        'SECONDARY_COLOR'
    ]

    def __init__(self, **data):
        self.data = data
        self.set_data()

    def set_data(self):
        for item in self.data.items():
            pass # hmm, i haven't quite figured out what exactly I want to do...

    # def update_team(self):




raw_team_data = requests.get("https://statsapi.web.nhl.com/api/v1/teams")

team_file_dir = os.path.join(os.path.abspath(os.path.join(os.path.curdir, os.path.pardir)),"teams.txt")
print(team_file_dir)
team_file = open(team_file_dir, "w")

team_file.write(raw_team_data.text)
team_file.close()
print(raw_team_data.text)
