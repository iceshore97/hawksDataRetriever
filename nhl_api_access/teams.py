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

        self.insert_into_db()

    def insert_into_db(self):
        # If the thing exists, use UPDATE, otherwise - USE INSERT
        check_select = "SELECT CODE FROM TEAMS WHERE ? = ?"
        history_database.database_connection.execute(check_select, self.CURRENT_DB_FIELD_MAPPINGS['abbreviation'], self.abbreviation)  # a little absurd, eh?
        if self.abbreviation == None:
            insert_statement = "INSERT INTO TEAMS (CODE, CITY, NAME) VALUES (?, ?, ?)"
        else:
            pass
        pass

    # def update_team(self):


# data_dict = {
#     'abbreviation': 'CHI',
#     'locationName': 'Chicago',
#     'teamName': 'Blackhawks'
# }
#
# blackhawks = Team(**data_dict)

raw_team_data = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
jsoned_data = json.loads(raw_team_data.content)
json_team_data = jsoned_data['teams']
print(json_team_data)

for team in json_team_data:
    print(team)

# team_file_dir = os.path.join(os.path.abspath(os.path.join(os.path.curdir, os.path.pardir)),"teams.txt")
# print(team_file_dir)
# team_file = open(team_file_dir, "w")
#
# team_file.write(raw_team_data.text)
# team_file.close()
# print(raw_team_data.text)
