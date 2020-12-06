import numpy as np 

class MAB:

    def __init__ (self,probs): #initial settings
        self.probs = probs
        self.tentativas = 0
        self.estimativa_prob = 1

    def alavanca(self): #gera um numero aleatorio e verifica se a probabilidade é menor que esse nr aleatório. em funçao deste vdd ou falso, ele vai iniciar outra maquina ou nao
        return np.random.random() < self.probs

    def update(self,x): #estimated probabilities for every new attempt. de cada vez que uma maq funciona, é chamada esta função que ajsuta a prob em funçao do nº de tentativas e do seu sucesso ou não
        self.tentativas +=1
        self.estimativa_prob = (self.estimativa_prob*(self.tentativas-1))/self.tentativas+x/self.tentativas



        
