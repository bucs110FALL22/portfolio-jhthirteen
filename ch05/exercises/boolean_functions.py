def percentage_to_letter(score):
  global letter
  if(score > 0 and score < 60):
    letter = 'F'
  elif(score >= 60 and score < 70):
    letter = 'D'
  elif(score >= 70 and score < 80):
    letter = 'C'
  elif(score >= 80 and score < 90):
    letter = 'B'
  elif(score >= 90):
    letter = 'A'
  return letter

def is_passing(letter):
  global passed
  if(letter == 'A' or letter == 'B' or letter == 'C'):
    passed = True
  else:
    passed = False
  return passed 

#Driver code:
def main():
  user_score = float(input("Enter your score for the class: "))
  user_letter = percentage_to_letter(user_score)
  user_pf = is_passing(user_letter)
  if(user_pf == True):
    print("You received a letter grade of ", user_letter, " in the class and you passed!")
  else:
    print("You received a letter grade of ", user_letter, " in the class and unfortunately failed")

main()