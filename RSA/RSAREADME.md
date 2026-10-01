# RSA Implementation learning summary

When learning the RSA in computational math, we learned a very dumbed down version where we used very small numbers. This meant we were able to try the basic concepts of key generation and encryption.  However, when I started my implementation of RSA, I realized that all the methods we used in lectures id not computationally viable, as RSA depended on using LARGE prime numbers to form the keys.

The following blog really helped me understand the mathametical concepts behind RSA, and give me most the hints on how to implement RSA successfully:
[Lei Mao's Log Book - RSA Algorithm](https://leimao.github.io/article/RSA-Algorithm/)

## The theory

I will only briefly mention the theory, if you are intersted, Lei Mai's blog explains the mathmatical theories behind why RSA work very throughly. Mainly, it utilizes the Euler's Theorem and Multiplicative Inverse Theorem to generate a unique private key from the public key.  While it is not very hard to compute the private key if you have all the information, it is impractical to compute the two large prime numbers that form n which is key to decrypting the message using modern computers, which makes RSA a relatively safe and strong encryption method.

## Execution
The first difficuly during implementation was generating the d value for the private key.  When we were doing the dumbed down practices in the lecture, we were able to obtain the multiplicative inverse by trying different multiples of e because the numbers were relatively very small, therefore it would not take too many tries to guess the right value of d.  However, practically n is made out of 2 LARGE prime numbers, therefore the numbers of tries needed to get the right value of d increases exponentially such that doing a value check while loop is not viable.

Here is where I had to learn the new concept of the extended euclidian algorithm, which is an extension of the euclidian algorithm used to find the gcd of 2 numbers.  When the extended algorithm is applied specifically to 2 co-prime numbers, the resulting sA + tB = 1 ( de + t(euler's totient function of n) = 1 ) gives de = 1 (mod (euler's totient function of n)) which by definition is the multiplicative inverse of e, giving us the correct value of d.

## Progress
- currently the encrypt and decrypt runs into runtime error, suspecting because using % on overly large number is taking too long, pending to implement own pow() function (yes there is an unbuilt pow() in python library but thats not fun)
- the random prime number generator is not efficient at bigger numbers which is used in practical enviroments and not truely random, researching better way to build it

