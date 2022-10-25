class Block:
  def __init__(self):
    self.is_mystery = False
    self.pattern = "Brick" #would have to have a way to input a brick texture
    self.is_interacted = False #establsihes if Mario hit/stands on block

class Goomba: 
  def __init__(self):
    self.body_color = (150,75,0) #makes body brown 
    self.start_health = 100
    self.hit_power = 10 #gives a value to the damage goomba can do to mario
    

class Mario:
  def __init__(self, x, y):
    self.hat_color = (255,0,0) #makes hat red
    self.position = (x, y) #coordinates passed to the class gives Mario a position 
    self.has_powerup = False
