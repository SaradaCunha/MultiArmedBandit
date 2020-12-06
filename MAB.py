import numpy as np 

class MAB:

    def __init__ (self,probs): #initial settings
        self.probs = probs
        self.tentativas = 0
        self.estimativa_prob = 1

    def alavanca(self): #arm
        return np.random.random() < self.probs

    def update(self,x): #estimated probabilities for every new attempt.
        self.tentativas +=1
        self.estimativa_prob = (self.estimativa_prob*(self.tentativas-1))/self.tentativas+x/self.tentativas



        
