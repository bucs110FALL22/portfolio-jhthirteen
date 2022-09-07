import turtle 

side_length = 50
square_angle = 90
my_screen = turtle.Screen()
my_screen.bgcolor("white")
my_turtle = turtle.Turtle()

my_turtle.shape("turtle")
my_turtle.color("purple")
for x in range(4):
  my_turtle.forward(side_length)
  my_turtle.right(square_angle)
my_turtle.color("red")
my_turtle.penup()
my_turtle.forward(25)
my_turtle.left(square_angle)
my_turtle.forward(25)
my_turtle.pendown()
for x in range(4):
  my_turtle.forward(side_length)
  my_turtle.right(square_angle)

my_screen.exitonclick()