class Rectangle:
  
  def __init__(self, x, y, h, w):
    if(x < 0): #If any var > x, automatically set to 0
      x = 0
    self.x = x
    if(y < 0):
      y = 0
    self.y = y
    if(h < 0):
      h = 0
    self.height = h
    if(w < 0):
      w = 0
    self.width = w
    
  def __str__(self):
    return f"(x: {self.x} y: {self.y}) height: {self.height} width: {self.width}"

