import random

class RSA:
    def __init__(self):
        self.p = 2
        self.q = 3
        self.n = self.p*self.q

    def pow(self, base, exp, mod):
        return base**exp - (base**exp//mod)*mod

    def key_generation(self):
        key = 0

test = RSA()
print(test.pow(3,2,4))
print((65537**-1)%((857504083339712752489993810777-1)*(1029224947942998075080348647219-1)))