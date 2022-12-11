from player import PlayerAPI
from games import NextgamesAPI

selected = False
while selected == False:
  #Asks user to enter a player, loops until they enter an actual player
  got_player = False
  while got_player == False:
    get_name = input("\nEnter a current NBA Player's full name: ")
    player = PlayerAPI(get_name)
    id = player.get()
    if id == 0:
      got_player = False
    else:
      got_player = True

  player.getTeam()
  player.getStats(id)
  player.formatStats()

  made_choice = False
  while made_choice == False:
    move_on_choice = input("Is this a player you would like to watch? (Enter Y for Yes or N for No): ")
    if move_on_choice == "Y":
      made_choice = True
      selected = True
    elif move_on_choice == "N":
      made_choice = True
    else: 
      print("Enter Y or N")

next = NextgamesAPI(player.teamname)
next.get()
next.getNextThreeGames()
for i in range(3):
  print("")
  next.getGameInfo(next.games[i], player.teamname)
  next.formatGameInfo(i)