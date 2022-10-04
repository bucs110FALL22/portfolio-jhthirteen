import turtle
import random 

#turtle/screen creation 
window = turtle.Screen()
#establish a size to have exact numbers for comparisons later 
window.screensize(400,400)
window.bgcolor('lightblue')
my_turtle = turtle.Turtle()
my_turtle.color('red')
my_turtle.shape('turtle')

#moves turtle to center of screen 
my_turtle.up()
my_turtle.goto(0,0)

on_screen = True
while(on_screen):
  #heads = 0 | tails = 1
  random_num = random.randrange(0,2)
  if(random_num == 0):
    my_turtle.left(90)
    my_turtle.forward(50)
  elif(random_num == 1):
    my_turtle.right(90)
    my_turtle.forward(50)
  #establishes x and y positions in variables to decide if they have gone off screen
  x_pos = my_turtle.xcor()
  y_pos = my_turtle.ycor()
  if(x_pos > 200 or x_pos < -200):
    on_screen = False
  elif(y_pos > 200 or y_pos < -200):
    on_screen = False

print("The turtle is off the screen!")