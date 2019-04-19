import sys, os, copy, sqlite3, requests



team_data = []
team_list = open('teams.txt','r') # not good!

for team in team_list:
    split_values = team.rstrip().split(" ")
    if len(split_values) > 5:
        new_value = '{} {}'.format(split_values[1], split_values[2])
        del split_values[1]
        split_values[1] = new_value
    team_data.append(split_values)

team_list.close()
print(team_data)

conn = sqlite3.connect('hawksHistory.db')
c = conn.cursor()

c.executemany("INSERT INTO TEAMS VALUES (?,?,?,?,?)", team_data)

conn.commit()
conn.close()