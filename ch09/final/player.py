import requests

class PlayerAPI:

  def __init__(self, name):
    self.url = f"https://www.balldontlie.io/api/v1/players?search={name}"

  def get(self):
    player_id = 0
    data = requests.get(self.url)
    response = data.json()
    self.player_data = response['data']
    if self.player_data == []:
      print("Not a player, please try again")
    else:
      player_id = self.player_data[0]['id']
    return player_id

  def getTeam(self):
    self.team = self.player_data[0]['team']
    self.teamname = self.team['full_name']

  def getStats(self, id):
    self.url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={id}"
    data = requests.get(self.url)
    response = data.json()
    stats = response['data']
    self.ppg = stats[0]['pts']
    self.apg = stats[0]['ast']
    self.rpg = stats[0]['reb']
    self.stl = stats[0]['stl']
    self.blk = stats[0]['blk']

  def formatStats(self):
    print("\nPLAYER OVERVIEW:")
    print("----------------")
    print(f"Team: {self.teamname}")
    print(f"Points per Game: {self.ppg}")
    print(f"Assists per Game: {self.apg}")
    print(f"Rebounds per Game: {self.rpg}")
    print(f"Steals per Game: {self.stl}")
    print(f"Blocks per Game: {self.blk}\n")