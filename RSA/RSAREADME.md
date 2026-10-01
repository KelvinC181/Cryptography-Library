# RSA Implementation learning summary

When learning the RSA in computational math, we learned a very dumbed down version where we used very small numbers. This meant we were able to try the basic concepts of key generation and encryption.  However, when I started my implementation of RSA, I realized that all the methods we used in lectures id not computationally viable, as RSA depended on using LARGE prime numbers to form the keys.

The following blog really helped me understand the mathametical concepts behind RSA, and give me most the hints on how to implement RSA successfully:
[Lei Mao's Log Book - RSA Algorithm](https://leimao.github.io/article/RSA-Algorithm/)

## The theory

I will only priefly mention the theory, if you are intersted, Lei Mai's blog explains the mathmatical theories behind why RSA work very throughly. Mainly, it utilizes the Euler's Theorem and Multiplicative Inverse Theorem to generate a unique private key from the public key.  While it is not very hard to compute the private key if you have all the information, it is impractical to compute the two large prime numbers that form n which is key to decrypting the message using modern computers, which makes RSA a relatively safe and strong encryption method.

## Execution

