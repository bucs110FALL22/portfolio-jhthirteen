#Part 1:

num_stars = int(input("Enter the number of stars you'd like printed "))
#Input variable to be called w/ the function, establishes number of starrs to be printed 

def star_pyramid(num_stars):
  for i in range(1, num_stars+1):
    print("*" * i)

print("")
star_pyramid(num_stars)

#Part 2:

num_starsr = int(input("Enter the number of stars you'd like printed for the reverse pyramid "))
#Input variable for the reverse function

def rstar_pyramid(num_starsr):
  for i in range(1, num_starsr+1):
    print("*" * num_starsr)
    num_starsr = num_starsr-1

print("")
rstar_pyramid(num_starsr)