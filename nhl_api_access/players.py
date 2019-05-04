from nhl_api_access import history_database
import os, requests, json

#Hawks only, for now
class Player:
    '''ha ha, he a player'''
    ATTRIBUTES = {
        'firstName': 'NAME',
        'lastName': 'SURNAME',
        'position': 'POSITION',
        'teamId': 'TEAM_ID'
    }

    def __init__(self):
        pass


player_json = requests.get("https://statsapi.web.nhl.com/api/v1/teams/16?expand=team.roster")
print(player_json.content)
