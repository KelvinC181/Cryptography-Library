import random
import sympy

class RSA:
    def __init__(self):
        self.p, self.q= self.prime_generator()
        self.n = self.p*self.q
        self.publicKey = (self.n, 65537)
        self.privateKey = (self.n, self.key_generation)

    def pow(self, base, exp, mod):
        return base**exp - (base**exp//mod)*mod

    def key_generation(self):
        euler_n = (self.p-1)*(self.q-1)

    def gcd(self,x,y):
        while x > 0:
            x,y = y, x%y
        return y
    
    def ext_euclidian_algo(self, A, B):
        '''
        this function tracks 2 equations:
        old_r = old_s * A + old_t * B  -> top
        r = s * A + t * B              -> bottom
        with each iteration, we go one step down in the euclidian algorithm
        to find a smaller and smaller remainder untill we reach the gcd

        the way to obtain the s,t value for each step is obtain by generalizing the q,r,s,t of each step of the euclidian algorithm

        we eventually have 
        gcd(A,B) = s * A + t * B

        returns the gcd, s, t
        '''

        #sets starting numbers
        old_s, old_t, s, t, old_r, r= 1, 0, 1, 0, A, B

        while r != 0:
            #moves the bottom tracked formula to the top, and computes the variables of the new bottom formula
            q = old_r//r
            old_r,r = r, old_r - q*r
            old_s, s = s, old_s - q*s
            old_t, t = t, old_t - q*t

        return old_r, old_s, old_t
    
    def prime_generator(self):
        primes = [i for i in range(1000,100000) if sympy.isprime(i)]
        p = random.choice(primes)
        q = random.choice(primes)
        while p == q:
            q = random.choice(primes)
        return p, q
    

test = RSA()
print(test.pow(3,2,4))
print(test.p)
print(test.q)
print(3120%17)