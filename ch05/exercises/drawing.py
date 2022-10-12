import turtle

#Setup
window = turtle.Screen()
window.bgcolor('lightblue')
my_turtle = turtle.Turtle()
my_turtle.color('green')
#Speed 1 allows users to visualize the animation 
my_turtle.speed(1)
num_sides = int(input("Enter the number of sides on the object you want the turtle to draw: "))
side_length = int(input("Enter the sides length for the object you want the turtle to draw: "))
#Moves turtle object to the center of the screen
turtle.penup()
turtle.goto(0,0)

def drawEqShape(turtle, num_sides, side_length):
  #Angle obtained by deviding number of sides by 360, then used to turn right when drawing the desired shape
  turn_angle = 360/num_sides
  turtle.pendown()
  #Looping through user's desired number of times
  for i in range(num_sides):
    turtle.forward(side_length)
    turtle.right(turn_angle)

drawEqShape(my_turtle, num_sides, side_length)
window.exitonclick()