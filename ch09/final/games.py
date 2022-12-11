import requests
from datetime import date, timedelta

class NextgamesAPI:
  def __init__(self, team):
    self.today = date.today()
    self.twoweeks = self.today + timedelta(weeks = 2)
    self.apikey = "MzA5MjU3NjJ8MTY3MDczMzMxNC45OTE3ODc"
    self.team = team.replace(' ', '-')
    self.url = f"https://api.seatgeek.com/2/events?performers.slug={self.team}&datetime_utc.gte={str(self.today)}&datetime_utc.lte={str(self.twoweeks)}&client_id={self.apikey}"

  def get(self):
    data = requests.get(self.url)
    response = data.json()
    self.event_data = response['events']

  def getNextThreeGames(self):
    self.games = []
    for i in range(0, 3):
      self.game_data = self.event_data[i]['id']
      self.games.append(self.game_data)

  def getGameInfo(self, game, team):
    self.url = f"https://api.seatgeek.com/2/events?id={game}&client_id={self.apikey}"
    data = requests.get(self.url)
    response = data.json()
    event = response['events']
    opponent_data = event[0]['performers']
    self.opponent = opponent_data[0]['name']
    if self.opponent == team:
      self.opponent = opponent_data[1]['name']
    venue_info = event[0]['venue']
    self.arena = venue_info['name_v2']

  def formatGameInfo(self, num):
    if num == 0:
      print("Next 3 Games Overview")
      print("---------------------")
    print(f"Opponent: {self.opponent}")
    print(f"Arena: {self.arena}")