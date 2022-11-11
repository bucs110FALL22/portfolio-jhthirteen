class StringUtility:
  
  def __init__(self, string):
    self.string = string
    self.length = len(self.string)

  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(self.length):
      for y in vowels:
        if (self.string[i].lower() == y):
          count = count + 1
    if (count < 5):
      return str(count)
    else:
      return "many"

  def bothEnds(self):
    new_string = ""
    two_from_end = self.length-2
    if(self.length <= 2):
      return ""
    else:
      for i in range(0, 2):
        new_string = new_string + self.string[i]
      for i in range(two_from_end, self.length):
        new_string = new_string + self.string[i]
      return new_string

  def fixStart(self):
    if(self.length <= 1):
      return ""
    else:
      str_list = list(self.string)
      first_char = str_list[0]
      for i in range(1, self.length):
        if(first_char == str_list[i]):
          str_list[i] = "*"
      new_string = ""
      for i in range(self.length):
        new_string = new_string + str_list[i]
      return new_string

  def asciiSum(self):
    str_list = list(self.string)
    sum = 0
    for i in range(self.length):
      num = ord(str_list[i])
      sum = sum + num
    return sum

  def cipher(self):
    has_spaces = False
    iterations = self.length
    
    #Determines if string has spaces
    for i in range(iterations):
      if(self.string[i] == " "):
        has_spaces = True
        break

    #Sets new "iterations" value (addition within cypher) if spaces are present
    if(has_spaces == True):
      iterations = iterations//2

    #Removes spaces
    if(has_spaces == True):
      for i in range(self.length):
        self.string = self.string.replace(" ", "")
        self.length = len(self.string)

    str_list = list(self.string)
    new_list = []
    revert_list = []
    values_to_change= []
    dict = {
      0: "a",
      1: "b",
      2: "c",
      3: "d",
      4: "e",
      5: "f",
      6: "g",
      7: "h",
      8: "i",
      9: "j",
      10: "k",
      11: "l",
      12: "m",
      13: "n",
      14: "o",
      15: "p",
      16: "q",
      17: "r",
      18: "s",
      19: "t",
      20: "u",
      21: "v",
      22: "w",
      23: "x",
      24: "y",
      25: "z"
    }

    #Actual "sorting" section
    for i in range(self.length):
      #All lowercase, stores value of uppercase letters to change
      if(str_list[i].isupper()):
        str_list[i] = str_list[i].lower()
        values_to_change.append(i)
      for y in dict:
        if(str_list[i] == dict[y]):
          z = y + iterations
          if(z >= 26):
            x = z - 26
            value = dict[x]
            new_list.append(value)
          else:
            value = dict[z]
            new_list.append(value)

    new_str = ""
    for i in range(self.length):
      for h in values_to_change:
        if(i == h):
          new_list[i] = new_list[i].upper()
      new_str = new_str + new_list[i]

    if(has_spaces == True):
      #Add spaces back to original string
      for i in range(self.length):
        revert_list.append(self.string[i])
        revert_list.append(" ")
      self.string = ""
      original_length = (self.length*2)-1
      for i in range(original_length):
        self.string = self.string + revert_list[i]
        
      str_list = []
      for i in range(len(new_str)):
        str_list.append(new_str[i])
        str_list.append(" ")
      str_list.pop(-1)
      new_str  = ""
      for i in range(len(str_list)):
        new_str = new_str + str_list[i]

    return new_str