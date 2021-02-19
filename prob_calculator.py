import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.balls = kwargs
    self.contents = []

    for k, v in self.balls.items():
      while v > 0:
        self.contents.append(k)
        v -= 1
  
  def draw(self, quantity):
    if quantity > len(self.contents):
      return self.contents
    
    response = []

    for i in range(quantity):
      id = random.randint(0, len(self.contents) - 1)
      response.append(self.contents[id]);
      self.contents.remove(self.contents[id])
    return response




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  n = 0

  while n < num_experiments:
    newHat = copy.deepcopy(hat)

    balls = newHat.draw(num_balls_drawn)
    
    drawnBalls = {}

    for color in balls:
      if drawnBalls.get(color) == None:
        drawnBalls[color] = 1
        continue
      drawnBalls[color] += 1
    
    match = True

    for k, v in expected_balls.items():
      if drawnBalls.get(k) == None or drawnBalls[k] < v:
        match = False
        break
    
    if match:
      m += 1
    n += 1
  
  return m/num_experiments
    
  