import turtle

my_screen = turtle.Screen()
my_screen.bgcolor("white")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

#Gets uesr input on number of sides and casts to an int
num_sides = int(input("Enter the number of sides for the shape you would like: "))
#User input for side length, float in case of decimal input
side_length = float(input("Enter the length each side should be: "))
#Allows users to select the color of the turtle
my_turtle.color(input("Enter the color you would like the turlte to draw in: "))
shape_angle = 360/num_sides

for _ in range(num_sides):
  my_turtle.forward(side_length)
  my_turtle.right(shape_angle)

my_screen.exitonclick()
  