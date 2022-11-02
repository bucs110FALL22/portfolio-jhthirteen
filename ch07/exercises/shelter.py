import time

class Animal:
  def __init__(self, name, animal_type):
    self.name = name
    self.type = animal_type
    self.id = time.strftime("%d%m%M%S")
    #Time always moving in a positive direction
    self.arrived = time.strftime("%m/%d/%Y")
    self.adopted = None
    
  def setAdopted(self): #called when the animal is adopted
    self.adopted = time.strftime("%m/%d/%Y")

  def __str__(self):
    result_str = f"{self.name} {self.type} \nArrived: {self.arrived} \nAdopted: {self.adopted}"
    return result_str
    

  
def main():
  charlie = Animal("charlie", "dog")
  charlie.setAdopted()
  print(charlie)
  
main()