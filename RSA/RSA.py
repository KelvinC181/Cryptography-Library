import random
import sympy
from tools.multInverse import multInverse
from tools.stringTranslation import stringTranslation

class RSA:
    def __init__(self):
        self.p, self.q= self.prime_generator()
        self.n = self.p*self.q
        self.publicKey = (self.n, 65537)
        self.privateKey = (self.n, self.private_key_generation())

    def pow(self, base, exp, mod):
        '''
        Binomial Exponentiation:
        in python, calculating x^n straight up takes n-1 calculations.  This is not a problem at lower powers,
        as n is small.  However, at larger n, e.g. 2^64, each multiplication takes longer and longer, amounting to a time complexity of ~O(n^2).

        Using binomial expoentiation, we only need to do at most log2(n) multiplications.  Moreover, by saving the base^2 and using that to multiply
        itself each time, it saves the n-1 multiplications needed to do exponents.  These 2 factors combine reduces the time complexity down to
        ~O(log(n)).

        applying it to mod arithmatic.
        this works because (A*B)modM = (AmodM * BmodM)modM
        in each iteration, we basically iterate through the binary representation of exp starting from the 2^0 unit:
        
        if the binary is 1:
            result = (result*base)%mod = (true_base^k modM * true_base^j modM)modM = (true_base^(k+j))modM

        base = (base*base)%mod = (true_base^k modM * true_base^k modM)modM = (true_base^2k)modM

        '''
        result = 1
        while exp != 0:
            if exp%2 == 1 :
                result = (result*base)%mod

            base = (base*base)%mod

            exp //= 2

        return result

    def private_key_generation(self):
        '''
        we get d by:
            ed = 1 (mod euler(n))
        '''
        euler_n = (self.p-1)*(self.q-1)
        return multInverse().multiplicative_inverse(65537, euler_n)

    def encrypt(self,message):
        return self.pow(message,self.publicKey[1],self.n)

    def decrypt(self,encrypted):
        return self.pow(encrypted,self.privateKey[1],self.n)

    
    def prime_generator(self):
        primes = [i for i in range(10000,99999) if sympy.isprime(i)]
        p = random.choice(primes)
        q = random.choice(primes)
        while p == q:
            q = random.choice(primes)
        return p, q
    

test = RSA()

encrypted_message = test.encrypt(100)
print(encrypted_message)
print(test.decrypt(encrypted_message))

translator = stringTranslation()
message = "abc"
encrypted_message2 = test.encrypt(translator.string_to_ascii(message))
print(encrypted_message2)
print(translator.ascii_to_string(test.decrypt(encrypted_message2)))