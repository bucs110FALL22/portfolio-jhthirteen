import turtle #1. import modules
import random
import pygame
import math 

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

# Race 1:
turtle.delay(100) #Slows down animations to help visualize the code 
distance1 = random.randrange(1,101)
distance2 = random.randrange(1,101)
michelangelo.forward(distance1)
leonardo.forward(distance2)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Race 2:
new_distance = random.randrange(0,11) #creates an initial random number for first movement  
for _ in range(10):
  leonardo.forward(new_distance)
  new_distance = random.randrange(0,11) #generating new distance between movements 
  michelangelo.forward(new_distance)
  new_distance = random.randrange(0,11) #again generating new distance
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
print("\nClick on the turtle game window to move on to part B of the lab!")
window.exitonclick() #clicking off moves to the pygame window

# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()
AQUAMARINE = (127, 255, 212, 255)
BLACK = (0,0,0,255)
coords = []
num_sides = 3
SIDE_LENGTH = 75
OFFSET = 150
count = 1 # Variable to change num_sides every integral of the loop starting on line 61

# Function that generates the x and y coordinates and returns them to be appended to the list of coordinates
def coord_gen(num_sides, SIDE_LENGTH, OFFSET, i):
  theta = (2.0*math.pi*(i))/num_sides
  x = SIDE_LENGTH*math.cos(theta) + OFFSET
  y = SIDE_LENGTH*math.sin(theta) + OFFSET
  return x,y

# Loop to create the shapes, increases constant for first 4, use of an if for the case of the circle
for z in range(5):
  for i in range(num_sides):
    cord = coord_gen(num_sides, SIDE_LENGTH, OFFSET, i)
    coords.append(cord)
  pygame.draw.polygon(window,AQUAMARINE,coords)
  pygame.display.flip()
  pygame.time.wait(1500) #1500 millisecond delay to actually see the shapes
  window.fill(BLACK)
  if(count==4): # Count hititng 4 indicates that the first 4 shapes have been drawn, and the circle has to follow
    num_sides = 360
    coords = []
  else:
    num_sides = num_sides + count
    count = count+1
    coords = []