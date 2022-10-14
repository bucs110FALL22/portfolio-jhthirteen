import pygame
pygame.init()

width = 400
height = 400
wait_time = 1000
display = pygame.display.set_mode((width, height))
#White
bg_color = (255, 255, 255)
#Black
font_color = (0,0,0)
font_size = 25
display.fill(bg_color)
pygame.display.flip()
font = pygame.font.Font(None, font_size)
upper_limit = 20
#Empty dictionary to eventually hold x,y coordinates
iters = {}
max_so_far = 0
max_val = 0
scale = 10

def threenseq(n):
  global count
  while(n != 1):
    if(n % 2 == 0):
      n = int(n/2)
      count = count + 1
    elif(n % 2 == 1):
      n = int((3*n)+1)
      count = count + 1
  return count

for i in range(2, upper_limit):
  display.fill(bg_color)
  pygame.display.flip()
  pygame.time.wait(wait_time)
  count = 0
  n = i
#Variable holds the return "count" variable
  num_iterations = threenseq(n)
  key, value = (i, num_iterations)
#Seperate valuables multiplied by the scale to appear larger when drawn into the GUI
  scale_key = key*scale
  scale_value = value*scale
  iters[scale_key] = scale_value
#Casts to a list so they can be added to drawing as a set of coordinates
  coords = list(iters.items())
#Needs to have 2 cases of coordinates for line to be drawn
  if(len(coords) >= 2):
    pygame.draw.lines(display, 'black', False, coords)
#Flips the y coordinate, line isn't updated until AFTER the flip 
  new_display = pygame.transform.flip(display, False, True)
  display.blit(new_display, (0,0))
  pygame.display.flip()
  if(value > max_so_far):
    max_so_far = value
    max_val = key
  final_message = "The highest iteration is " + str(max_so_far) + " at the value of " + str(max_val)
  graph_display = font.render(final_message, True, 'black')
  display.blit(graph_display, (10,10))
  pygame.display.flip()
  pygame.time.wait(wait_time)

#User has to control + c in the shell to close the display 
running = True
while(running):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False