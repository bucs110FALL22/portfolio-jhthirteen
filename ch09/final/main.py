from player import PlayerAPI
from games import NextgamesAPI

def main():
  selected = False
  while selected == False:
    #Asks user to enter a player, loops until they enter an actual player
    got_player = False
    while got_player == False:
      get_name = input("\nEnter a current NBA Player's full name: ")
      player = PlayerAPI(get_name)
      id = player.get()
      #In the case of the user not entering an actual player
      if id == 0:
        got_player = False
      else:
        got_player = True

    player.getTeam()
    player.getStats(id)
    player.formatStats()

    #Gives the opportunity to choose again
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

  #Gets info for next 5 games and formats it into a visually pleasing output
  next = NextgamesAPI(player.teamname)
  next.get()
  next.getNextFiveGames()
  for i in range(5):
    print("")
    next.getGameInfo(next.games[i], player.teamname)
    next.formatGameInfo(i)

  game_choice_made = False
  #Checks if choice is one of the five possibilities
  while game_choice_made == False:
    game_num = int(input("\nEnter the number game you would like to attend: "))
    if(game_num > 0 and game_num < 6):
      game_chioce_made = True
      break
    else:
      print("\nPlease choose either game 1, 2, 3, 4, or 5")

  #Generates ticket information
  next.getTicketUrl(game_num, player.teamname)

main()