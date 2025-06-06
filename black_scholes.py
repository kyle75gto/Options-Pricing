import numpy as np
from scipy.stats import norm
from abc import ABC, abstractmethod

class Option(ABC):
    def __init__(self, S, K, T, r, sigma):
        self.S = S       
        self.K = K       
        self.T = T       
        self.r = r      
        self.sigma = sigma 

    def d1(self):
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)
    
    def price(self):
        pass

    def delta(self):
        pass
        
    def gamma(self):
        return round(norm.pdf(self.d1()) / (self.S * self.sigma * np.sqrt(self.T)),2)

    def vega(self):
        return round(self.S * norm.pdf(self.d1()) * np.sqrt(self.d1()),2)

    def theta(self):    
        pass

    def rho(self):
        pass