import numpy as np
from scipy.stats import norm
from black_scholes import Option


class Call(Option):
    def __init__(self,S,K,T,r,sigma):
        super().__init__(S,K,T,r,sigma)
    
    def price(self):
        return round(self.S * norm.cdf(self.d1()) - self.K * np.exp((-self.r * self.T)) * norm.cdf(self.d2()),2)
    
    def delta(self):
        return round(norm.cdf(self.d1()),2)
    
    def theta(self):
        left = -self.S * norm.pdf(self.d1()) * self.sigma / (2 * np.sqrt(self.T))
        right = -self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2())
        return round(left + right,2)
    
    def rho(self):
        return round(self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.d2()),2)

class Put(Option):
    def __init__(self,S,K,T,r,sigma):
        super().__init__(S,K,T,r,sigma)

    def price(self):
        return round(self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2()) - self.S * norm.cdf(-self.d1()),2)
    
    def delta(self):
        return round(norm.cdf(self.d1())-1,2)
    
    def theta(self):
        left = -self.S * norm.pdf(self.d1()) * self.sigma / (2 * np.sqrt(self.T))
        right = -self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2())
        return round(left + right,2)
    
    def rho(self):
        return round(self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-self.d2()),2)

# class Portfolio():
#     def __init__(self):
#         self.options = []

# class Straddle(Portfolio):
#     def __init__(self, )