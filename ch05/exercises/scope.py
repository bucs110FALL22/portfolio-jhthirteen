def multiplyTwo(num1, num2):
  result = 0
  for i in range(num2):
    result = result + num1
  return result

def exponentiation(num, exponent):
  result = 1
  for i in range(exponent):
    result = result * num
  return result

def square(num):
  return multiplyTwo(num, num)

def main():
  part_one = multiplyTwo(8, 4)
  print(part_one)
  part_two = exponentiation(4, 3)
  print(part_two)
  part_three = square(9)
  print(part_three)

main()