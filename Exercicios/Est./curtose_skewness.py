import math
from scipy import stats, ndimage
import numpy as np

class Vec:
    def __init__(self, dados = None):
        self.data = dados

    def push(self, value_vec: list = None, value = None):
        # if not value_vec and not value:
        #     return
        return

    def curtose(self):
        return (self.central_moment(4) / (self.std() ** 4)) - 3

    def std(self):
        if not self.data:
            return
        
        n = len(self.data)
        mean = sum(self.data) / n

        dif = 0
        for d in self.data:
            dif += (d - mean) ** 2

        return math.sqrt(dif/n)

    def var(self, ddof=1):
        if not self.data:
            return
        
        n = len(self.data)
        mean = sum(self.data) / n

        dif = 0
        for d in self.data:
            dif += (d - mean) ** 2
        
        return dif/(n - ddof)
    
    def mean(self):
        return sum(self.data) / len(self.data)

    def central_moment(self, k):
        if not self.data:
            return

        n = len(self.data)
        mean = sum(self.data) / n

        ct_momen = 0
        for d in self.data:
            q = self.data.count(d)
            ct_momen += (q/n) * ((d - mean) ** k)
        
        return ct_momen

    def skewness(self, fisher = False):
        if not self.data:
            return
        
        corr = 1
        n = len(self.data)
        mean = self.mean()
        if fisher:
            corr = math.sqrt(n * (n-1)) / (n-2)
        else:
                dif = 0
                for d in self.data:
                    dif += ((d - mean)**3) / n

        return corr*dif / self.std()**3
def main():
    data = [1, 2, 3, 4, 5, 10, 15]
    vec = Vec(data)
    kurt_scipy = stats.kurtosis(data, bias=True, fisher=True)

    print(vec.curtose(), kurt_scipy)
    print(vec.std(), ndimage.standard_deviation(data))
    print(vec.skewness(), stats.skew(data))





main()