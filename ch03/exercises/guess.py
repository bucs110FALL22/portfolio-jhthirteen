import random 

target_num = random.randrange(1,11)
num_guesses = 0
right_wrong = False #flag to determine if the script should print right/wrong message
for _ in range(3):
  user_guess = int(input("Guess a number 1-10: "))
  num_guesses += 1
  if (user_guess > target_num):
    print("Too High")
  elif(user_guess < target_num):
    print("Too Low")
  else:
    print("Correct")
    right_wrong = True 
    break
if (right_wrong == False):
  print("You did not guess the number right!")
else: 
  print("It took you", num_guesses, "to get it right!")