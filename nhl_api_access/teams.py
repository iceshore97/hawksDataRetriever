from nhl_api_access import history_database
import sqlite3, os, requests, json


class Team:

    CURRENT_DB_FIELD_MAPPINGS = {
        'abbreviation': 'CODE',
        'locationName': 'CITY',
        'teamName': 'NAME',
        # 'MAIN_COLOR',
        # 'SECONDARY_COLOR'
    }

    def __init__(self, **data):
        for key in data:
            if key in self.CURRENT_DB_FIELD_MAPPINGS.keys():
                setattr(self, key, data[key])

    def insert_into_db(self):
        # If the thing exists, use UPDATE, otherwise - USE INSERT
        check_tuple = (self.CURRENT_DB_FIELD_MAPPINGS['abbreviation'], self.abbreviation) # dat fuckin naming, tho...
        check_select = "SELECT CODE FROM TEAMS WHERE ? = ?"
        history_cursor = history_database.database_connection.cursor()
        history_cursor.execute(check_select, check_tuple)  # a little absurd, eh?
        check_row = history_cursor.fetchone()
        print(check_row)
        # yoo, this makes no sense in relation to the check one line up:
        if check_row is None:
            print("uno")
            insert_statement = "INSERT INTO TEAMS (CODE, CITY, NAME, MAIN_COLOR, SECONDARY_COLOR) VALUES (?, ?, ?, ?, ?)"
            insert_tuple = (self.abbreviation, self.locationName, self.teamName, None, None)
            history_cursor.execute(insert_statement, insert_tuple)
            history_database.database_connection.commit()
        else:
            print("dos")
            self.update_team()

    def update_team(self):
        update_select = "UPDATE TEAMS SET CITY = ?, NAME = ? WHERE CODE = ?"


raw_team_data = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
jsoned_data = json.loads(raw_team_data.content)
json_team_data = jsoned_data['teams']

team_list = []
for team in json_team_data:
    team_dict = {
        'abbreviation': team['abbreviation'],
        'locationName': team['locationName'],
        'teamName': team['teamName']
    }
    team_list.append(team_dict)

team_list.sort(key=lambda team: team['abbreviation']) # Maaate, this is so sweet! Gotta learn more about lambdas, tho

for team in team_list:
    next_team = Team(**team)
    print(next_team.abbreviation)
    next_team.insert_into_db()



# team_file_dir = os.path.join(os.path.abspath(os.path.join(os.path.curdir, os.path.pardir)),"teams.txt")
# print(team_file_dir)
# team_file = open(team_file_dir, "w")
#
# team_file.write(raw_team_data.text)
# team_file.close()
# print(raw_team_data.text)
