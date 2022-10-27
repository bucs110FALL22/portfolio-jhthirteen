import turtle


def get_coords(my_turtle):
  
  '''
  obtains the x and y coordiantes of the turtle
  args: (turtle.Turtle) turtle object which is having its coords generated
  return: (int) x position and y position in the form of a tuple
  '''
  
  x_cord = my_turtle.xcor()
  y_cord = my_turtle.ycor()
  return (x_cord, y_cord)


def draw_rect(my_turtle, width, height, x, y, color):
  
  '''
  draws a rectangle, used for skyscrapers, windows, doors, and roof
  args: (turtle.Turtle, int, int, int, int, str) turtle obj to draw, width and height used for rect paramaters, x and y used to move to desired pos, color for desired shape color
  return: None
  '''

  my_turtle.pu() #Setup
  my_turtle.goto(x, y)
  my_turtle.pd()
  iters = 2 #Rectangle needs two loop iterations (diff height/widths)
  angle = 90 #Turn angle is a constant, always 90 degrees
  my_turtle.fillcolor(color)
  my_turtle.begin_fill()
  
  for i in range(iters): #Drawing of rect
    my_turtle.forward(width)
    my_turtle.right(angle)
    my_turtle.forward(height)
    my_turtle.right(angle)
    
  my_turtle.end_fill()
  my_turtle.pu()


def draw_windowset(my_turtle, width, height, color):
  
  '''
  draws a set of 2 x num_windows set of windows on a skyscraper
  args: (turtle.Turtle, int, int, str) turtle obj to draw, width and height to be manipulated into a value to offset the windows and assign a fitting length to them, color for desired window color
  return: None
  '''
  
  offset = width/12 #Offset used to establish a distance between the wall and the window
  window_length = width/3 #Proportionally cuts down the size of the windows by the size of the skyscraper
  (x, y) = get_coords(my_turtle)
  num_windows = (height / ((2 * offset) + window_length)) #Long equation divides height by the total distance each window has, rounds down to give the most fitting num of windows 
  
  for i in range(int(num_windows)): #Drawing of windows
    draw_rect(my_turtle, window_length, window_length, x+offset, y-offset, color)
    draw_rect(my_turtle, window_length, window_length, x+((offset*3)+window_length), y-offset, color)
    y = y - 30 #Allows turtle to draw windows down the skyscraper
    my_turtle.pu()
    my_turtle.goto(x, y)   


def draw_circlewindow(my_turtle, x, y, radius, color):
  
  '''
  draws a circular window on a skyscraper
  args: (turtle.Turtle, int, int, int, str) turtle obj to draw, x and y to establish location of circle, radius is width / 4 for a good fit, color for desired window color
  return: None
  '''
  
  radius = radius/4 #Makes the window nicely fit on skyscraper
  my_turtle.pu()
  my_turtle.goto(x, y) #Move to center and upper region
  my_turtle.pd()
  my_turtle.fillcolor(color) 
  my_turtle.begin_fill()
  my_turtle.circle(radius) #Drawing of window 
  my_turtle.end_fill()
  my_turtle.pu()


def draw_roof_one(my_turtle, width, height, color):
  
  '''
  draws roof v1, which is a smaller, flat rect and a taller, skinny rect 
  args: (turtle.Turtle, int, int, str) turtle obj to draw, width and height to determine an offset for both rects on the roof and get proportionate widths and heights for each rect, color for desired roof color
  return: None
  '''
  
  (x,y) = get_coords(my_turtle)
  offset = width/12
  roof_width = width - (offset*2)
  roof_height = height/25
  draw_rect(my_turtle, roof_width, roof_height, x+offset, y+(offset*2), color) #Draws long, short rect
  draw_rect(my_turtle, offset*2, roof_width, x+(offset*5), y+(offset*8), color) #Draws tall, skinny rect


def draw_roof_two(my_turtle, width, color):
  
  '''
  draws roof v2, which is an equilateral triangle w/ three 60 degree angles, and sides the same length as the width of the skyscraper it is attached to 
  args: (turtle.Turtle, int, str) turtle obj to draw, width used to determine the length of the triangles sides, color for desired roof color 
  return: None
  '''
  
  my_turtle.color(color)
  num_sides = 3
  angle = 180/num_sides #Establishes 60 degree angle
  my_turtle.left(angle) #Slight 60 degree shift to get the turtle on triangular path
  my_turtle.begin_fill()
  
  for i in range(num_sides): #Drawing of roof
    my_turtle.forward(width)
    my_turtle.right(angle*2) #Has to turn a full 120 degrees
    
  my_turtle.end_fill()
  my_turtle.pu()
  my_turtle.right(angle) #Re-establishes turtle to correct angle


def draw_door(my_turtle, width, height, x, y, color):
 
  '''
  draws a door at the base of a skyscraper
  args: (turtle.Turtle, int, int, int, int, str) turtle obj to draw with, width and height to create a door offset from building, and new door heights/widths in proportion w/ skyscraper, x and y to position the door, color for desired door color
  return: None
  '''
  
  offset = width/4
  door_height = height/6
  door_width = width/2
  dist_from_top = height-door_height #Where to start the door height wise
  draw_rect(my_turtle, door_width, door_height, x+offset, y-dist_from_top, color) #Drawing of door

  
def draw_skyscraper(my_turtle, width, height, turn_angle, window_type, has_roof, roof_type, has_door, x, y): #Longer function, very conditional so it can be used for dif skyscrapers
 
  '''
  draws a skyscraper, allows there to be different roofs, windows, and the option of a door
  args: (turtle.Turtle, int, int, int, int, bool, int, bool, int, int) turtle to draw, width and height for the building itself, turn angle (usually 90) for turns in rect drawing, window_type num is conditional, correlates to either the panels or the circle, has_roof determines if a roof should be drawn, if it should roof_type determines which roof (1 or 2) is drawn, has_door determines if a door is drawn, and x and y pass coordinates to other functions as paramaters
  return: None
  '''

  skyscraper_color = 'black'
  window_color = 'yellow'
  door_color = 'lightblue'
  
  draw_rect(my_turtle, width, height, x, y, skyscraper_color)
  
  if(window_type == 1): #Determines which set of windows to draw
    draw_windowset(my_turtle, width, height, window_color)
  elif(window_type == 2):
    draw_circlewindow(my_turtle, x+(width/2), y-(height/3), width, window_color)
  
  if(has_roof == True): #Determines which roof to draw
    my_turtle.goto(x, y) #Reset to skyscraper origin
    if(roof_type == 1):
      draw_roof_one(my_turtle, width, height, skyscraper_color)
    elif(roof_type == 2):
      draw_roof_two(my_turtle, width, skyscraper_color)
  
  if(has_door == True): #Determines if a door should be drawn
    draw_door(my_turtle, width, height, x, y, door_color)

    
#Driver Code
def main():
  
  window = turtle.Screen() #Setup
  window.screensize(200,400) #Enter fullscreen on the repl output
  window.bgcolor('purple')
  my_turtle = turtle.Turtle()
  (x, y) = get_coords(my_turtle)
  
  draw_skyscraper(my_turtle, 60, 250, 90, 1, True, 1, False,  x-200, y+50) #Skyscraper 1
  my_turtle.goto(x,y)
  draw_skyscraper(my_turtle, 80, 150, 90, 2, True, 2, False, x-100, y-50) #Skyscraper 2
  my_turtle.goto(x,y)
  draw_skyscraper(my_turtle, 72, 312, 90, 1, False, 0, True, x+100, y+112) #Skyscraper 3
  
  window.exitonclick()

main()