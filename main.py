import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def __str__(self):
        return str(self.contents)

    def draw(self, num):
        balls_drawn = []
        if len(self.contents) < num:
            balls_drawn = copy.copy(self.contents)
            self.contents.clear()
            return balls_drawn
      
        for _ in range(num):
            ele = random.choice(self.contents)
            self.contents.remove(ele)
            balls_drawn.append(ele)
        return balls_drawn
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    exp = []
    count = 0
    r =0
    for k,v in expected_balls.items():
        for _ in range(v):
            exp.append(k)
    
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        drawn = h.draw(num_balls_drawn)
        #print(drawn)
        #print(exp, "exp")
        cop_exp = copy.deepcopy(exp)
        #print(cop_exp)
        for ele in drawn:
            if ele in cop_exp:
                cop_exp.remove(ele)
                #list(drawn).remove(ele)
        if len(cop_exp) == 0:
            count +=1
        
                
      
    return count / num_experiments



hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=200)
print(probability)