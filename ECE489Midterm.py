#RSA Examples 
# Based off HW 3 in ECE 489/549 

# RSA as HW #5: Verify your code by encrypting and decrypting the two examples in your answers of HW #5.

# Two major components of your code: Given p & q (prime) & e (relative prime to z)
# 1)	Extended Euclid(z, e): find d (create two keys)
# 2)	Reduce Calculation (Base, n, e, max): deal with overflow of exponent & mod
# for example: Base = C = 128, n = 527, e = 343 (or d), max = 150
# e = quotient * max + remainder: 343 = 2 * 150 + 34
# 128343 mod 527 = (128150 mod 527)2 * (12843 mod 527)

import math 
# print("Please enter the 'p' and 'q' values:")
#     p = int(input("Enter a prime number for p: "))
#     q = int(input("Enter a prime number for q: "))

# def computeGCD(x, y): 
#      if x > y: 
#          small = y 
#      else: 
#         small = x 
#      for i in range(1, small+1): 
#         if((x % i == 0) and (y % i == 0)): 
#              gcd = i 
#      return gcd 
# let p = 3
# let q = 11
# let e = 7
# let m = 5 


 

def eea(z,e): #extended euclid algorithm 
    a1= 1
    a2= 0 
    a3= z
    b1= 0  
    b2= 1
    b3= e
    t1= b1  
    t2= b2
    t3= b3
    d= t2
    while(d != 1):
        q=math.floor(a3/b3)
        print(d)

        t1= a1-t1*q
        t2= a2-t2*q
        d= t2
        t3= a3-t3*q
        a1= t1
        a2= t2 
        a3= t3
    
    
    #create a variable t for temporary, then calculate b's 
    #ehile b3 =! 1 , stay in loop 
        # floor(An/bn)
    #t1=b1. t2=b2. t3=b3

eea(20,7)

# def RSAencrypt(p,q,e,m):
#     n=p*q
#     print("n= ", n)
#     z=(p-1)*(q-1)
#     print("z= ", z)
#     d = (e^(-1)) % z
#     print("d= ",  d)
#     verifyd= d*e % z 
#     print("Verify d = ",verifyd)

    

#     ku=[n,e]
#     print("KU = ", ku)
#     kr=[n,d]
#     print("Kr = ", kr)

#     encryptedM = (m^ku[1]) % ku[0]
#     decryptedM= (encryptedM^kr[1]) % kr[0]
#     return(encryptedM, decryptedM)
    

# [encryptedMessage , decryptedMessage] = RSAencrypt(3,11,7,5)
# print("encrypted message =", encryptedMessage)
# print("decrypted message =", decryptedMessage)