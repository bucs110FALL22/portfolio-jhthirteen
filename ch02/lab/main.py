import random 

#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
#prints cost per week (tuition price divided by num classes, then divided by weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
#divides the previous cost value by classes in a week and prints the value 
print("Cost per class: ", cost_per_class, type(cost_per_class))

#Part B
my_list = ["cat", "dog", "fish", "bird", "snake"]
random_animal = random.choice(my_list)
print("Your random animal is a", random_animal)