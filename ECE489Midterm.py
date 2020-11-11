#RSA Examples 
# Based off HW 5 in ECE 489/549 
# RSA as HW #5: Verify your code by encrypting and decrypting the two examples in your answers of HW #5.

import math 


def eea(z,e): #extended euclid algorithm 
    print("__________________BEGIN EXTENDED EUCLIDEAN ALGORITHM_____________________")
    a1= 1
    a2= 0 
    a3= z
    print("a1 =", a1)
    print("a2 =", a2)
    print("a3 =", a3, "\n")

    b1= 0  
    b2= 1
    b3= e
    print("b1 =", b1)
    print("b2 =", b2)
    print("b3 =", b3)

    t1= b1  
    t2= b2
    t3= b3

    q=math.floor(a3/t3)
    while(b3 > 1):
        print("\nb3 = ", b3)
        q=math.floor(a3/b3)
        print("q=", q)
        print("________")

        print("a1 =", t1)
        print("a2 =", t2)
        print("a3 =", t3, "\n")

        b1= a1-(t1*q)
        b2= a2-(t2*q)  
        b3= a3-(t3*q)
        
        print("b1 =", b1)
        print("b2 =", b2)
        print("b3 =", b3, "\n")
        
        a1= t1
        a2= t2 
        a3= t3

        t1= b1  
        t2= b2
        t3= b3
        


    # while(b3 > 1):
    #     print("\nb3 = ", b3)
    #     q=math.floor(a3/b3)
    #     print("q=", q)
    #     print("________")


        
    #     print("a1 =", t1)
    #     print("a2 =", t2)
    #     print("a3 =", t3, "\n")

    #     b1= a1-(t1*q)
    #     b2= a2-(t2*q)  
    #     b3= a3-(t3*q)
        
    #     print("b1 =", b1)
    #     print("b2 =", b2)
    #     print("b3 =", b3, "\n")

    #     t1= b1  
    #     t2= b2
    #     t3= b3
        
    #     a1= t1
    #     a2= t2 
    #     a3= t3        
    


    #create a variable t for temporary, then calculate b's 
    #ehile b3 =! 1 , stay in loop 
        # floor(An/bn)
    #t1=b1. t2=b2. t3=b3
    print("_______________________________END ALGORITHM______________________________")

    return(b2)
eea(20,7)

def RSAencrypt(p,q,e,m):
    print("p,q,e,m =", p,q,e,m)
    n=p*q
    print("n= ", n)
    z=(p-1)*(q-1)
    print("z= ", z)
    d = eea(z,e)  # 3
    print("d= ",  d)

    ku=[n,e]
    print("Ku = ", ku)
    kr=[n,d]
    print("Kr = ", kr)

    encryptedM = (m**ku[1]) % ku[0]
    decryptedM = (encryptedM**kr[1]) % kr[0]

    return(encryptedM, decryptedM)

def RSAencrypt2(p,q,e,m):
    print("p,q,e,m =", p,q,e,m)
    n=p*q
    print("n= ", n)
    z=(p-1)*(q-1)
    print("z= ", z)
    d = eea(z,e) % 480 #-137 % 480
    print("d= ",  d)

    ku=[n,e]
    print("Ku = ", ku)
    kr=[n,d]
    print("Kr = ", kr)

    encryptedM = (m**ku[1]) % ku[0]
    decryptedM = (encryptedM**kr[1]) % kr[0]
    return(encryptedM, decryptedM)

print("1.	p = 3 & q = 11, e = 7; M = 5 ")
[encryptedMessage , decryptedMessage] = RSAencrypt(3,11,7,5)
print("encrypted message =", encryptedMessage)
print("decrypted message =", decryptedMessage, "\n")

print("2.	p = 17 & q = 31, e = 7; M = 2")
[encryptedMessage2 , decryptedMessage2] = RSAencrypt2(17,31,7,2)
print("encrypted message =", encryptedMessage2)
print("decrypted message =", decryptedMessage2)