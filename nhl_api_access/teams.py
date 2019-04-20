import os, requests, json

raw_team_data = requests.get("https://statsapi.web.nhl.com/api/v1/teams")

team_file_dir = os.path.join(os.path.abspath(os.path.join(os.path.curdir, os.path.pardir)),"teams.txt")
print(team_file_dir)
team_file = open(team_file_dir, "w")

team_file.write(raw_team_data.text)
team_file.close()
print(raw_team_data.text)

