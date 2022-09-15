import random 

target_num = random.randrange(0,10,1)
for _ in range(3):
  user_guess = int(input("Guess a number 1-10: "))
  if (user_guess > target_num):
    print("Too High!")
  elif(user_guess < target_num):
    print("Too Low!")
  else:
    print("Correct!")
    break