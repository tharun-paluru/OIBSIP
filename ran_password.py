#python program to generate a random passworn in which user can select the password length and characters of the password

import random
import string

len = int(input("enter the length of the password to be generated:")) #length of password to be generated
num = int(input("enter '1' if you want to include digits(0 to 9) in your password else enter '0':")) 
small_alpa = int(input("enter '1' if you want include small alphabets(lower case letters i.e a to z) in your password else enter '0':"))
cap_alpa = int(input("enter '1' if you want include CAPITAL ALPHABETS(upper case letters i.e A to Z) in your password else enter '0':"))
spl_sym = int(input("enter '1' if you want to include special symbols ( ['!','@','#','$','%','^','&','*','_','-','~','+',etc...]) in your password else enter '0':"))

ran=[]                                                      #empty list for password
digits = [chr(c) for c in range(48,58)]                     #list of digits (0,9)
upcase_let = [chr(i) for i in range (65,91)]                #list of small alphabets(a,z)
lowcase_let = [chr(j) for j in range (97,123)]              #list of capital alphabets(A,Z)
sym = string.punctuation                                    #list of special symbols

#generating password
print("length of the password is:",len)
while len>0:
    if(num == 1):
        ran.append(random.choice(digits))
        len -=1
        if len <= 0:
            break
    if(small_alpa == 1):
        ran.append(random.choice(lowcase_let))
        len -=1
        if len <= 0:
            break
    if(cap_alpa == 1):
        ran.append(random.choice(upcase_let))
        len -=1
        if len <= 0:
            break
    if(spl_sym == 1):
        ran.append(random.choice(sym))
        len -=1
        if len <= 0:
            break

#printing the password
print("the random password is:",end=" ")
for n in ran:
    print(n,end="")