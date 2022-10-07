import pygame 
import random
import math 

#Part A: Setup 
pygame.init()
WIDTH = 400
HEIGHT = 400
#window initialized globally so it can be used outside of the method the board is created in 
window = pygame.display.set_mode((WIDTH, HEIGHT))
size_variables = pygame.display.get_window_size()
width = size_variables[0]
height = size_variables[1]

#Function that creates the board so it can be called twice in the program 
def board_creation():
  window.fill('yellow')
  pygame.display.flip()
  
#Creation of dart board 
  pygame.draw.circle(window, 'black', (200,200), 200)
  pygame.display.flip()
  pygame.draw.circle(window, 'green', (200, 200), 198)
  pygame.display.flip()
  pygame.draw.line(window, 'black', (199,0), (199,400), 2)
  pygame.display.flip()
  pygame.draw.line(window, 'black', (0,199), (400,199), 2)
  pygame.display.flip()

board_creation()

#Part B: Throwing Darts
#Range 10 simulates ten turns
for i in range(10):
  #Random x and random y coordinate to create a circle, simulates a "throw"
  dart_x = random.randrange(0, WIDTH)
  dart_y = random.randrange(0, HEIGHT)
  distance_from_center = math.hypot(HEIGHT/2-dart_x, WIDTH/2-dart_y)
  is_in_circle = distance_from_center <= WIDTH/2
#If it's true that it is in the cirlce, the dot is blue
  if(is_in_circle == True):
    pygame.draw.circle(window, 'blue', (dart_x, dart_y), 4)
    pygame.display.flip()
    pygame.time.wait(800)
#If it's false that it is in the circle, the dot is red
  elif(is_in_circle == False):
    pygame.draw.circle(window, 'red', (dart_x, dart_y), 4)
    pygame.display.flip()
    pygame.time.wait(800)

#Part C: A Game of Darts
#Resets the board
window.fill('black')
pygame.display.flip()
#Creates two boxes, a red and a blue for user selection with mouse
red_rect = pygame.Rect(40,40,100,100)
pygame.draw.rect(window, 'red', red_rect)
pygame.display.flip()
blue_rect = pygame.Rect(220,40,100,100)
pygame.draw.rect(window, 'blue', blue_rect)
pygame.display.flip()

#Prints to the shell, provides basic instruction for the actual game
print("\nSelect either player red or player blue using your mouse (by clicking their square). Who do you think will win?")
print("Basic Rules: Each player alternates, a red dot is a point for red, a blue dot is a point for blue. A purple dot is a miss for either players.")

selection_wait = True
user_selection = 'None'
while(selection_wait):
  for event in pygame.event.get():
    if(event.type == pygame.MOUSEBUTTONDOWN):
      current_mouse_loc = pygame.mouse.get_pos()
      (x, y) = current_mouse_loc
#Hitboxes established in the button coordinates, if the mouse is clicked in said box range, than it is selected
      if((x >= 40 and x <= 140) and (y >= 40 and y <= 140)):
        user_selection = 'red'
        selection_wait = False
      elif((x >= 220 and x <= 320) and (y >= 40 and y <= 140)):
        user_selection = 'blue'
        selection_wait = False
#If they misclick, the loop continues and prompts them to reselect
      else:
        print("Please select one of the boxes")
        continue 

board_creation()
red_score = 0
blue_score = 0
#Use of the % function (=0 or =1) to determine if it is red or blues turn
counter = 1

#Repeated section when they miss, because the color is constant regardless of who shoots 
def missed_shot(x,y):
  pygame.draw.circle(window, 'purple', (x, y), 4)
  pygame.display.flip()
  pygame.time.wait(800)
  
#Red vs. Blue game 
for i in range(20):
#Loop very similar to part b, just more possibilities now and alternating colors 
  dart_x = random.randrange(0, WIDTH)
  dart_y = random.randrange(0, HEIGHT)
  distance_from_center = math.hypot(HEIGHT/2-dart_x, WIDTH/2-dart_y)
  is_in_circle = distance_from_center <= WIDTH/2
  if(counter % 2 == 1):
    if(is_in_circle == True):
      pygame.draw.circle(window, 'red', (dart_x, dart_y), 4)
      pygame.display.flip()
      pygame.time.wait(800)
      red_score = red_score + 1
      counter = counter + 1
    elif(is_in_circle == False):
      missed_shot(dart_x, dart_y)
      counter = counter + 1
  elif(counter % 2 == 0):
    if(is_in_circle == True):
      pygame.draw.circle(window, 'blue', (dart_x, dart_y), 4)
      pygame.display.flip()
      pygame.time.wait(800)
      counter = counter + 1
      blue_score = blue_score + 1
    elif(is_in_circle == False):
      missed_shot(dart_x, dart_y)
      counter = counter + 1

#Results Page
print("")
if((red_score > blue_score) and user_selection == 'red'):
  print("Player red has won")
  print("Congratulations! You guessed correctly!")
elif((red_score < blue_score) and user_selection == 'blue'):
  print("Player red has won")
  print("Sorry, you guessed incorrectly")
elif((blue_score > red_score) and user_selection == 'blue'):
  print("Player blue has won")
  print("Congratulations! You guessed correctly!")
elif((blue_score > red_score) and user_selection == 'red'):
  print("Player blue has won")
  print("Sorry, you guessed incorrectly")
else:
  print("Player red and player blue have tied!")