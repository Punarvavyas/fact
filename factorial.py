import math
import fileinput
import random


f= open("factorial.txt",'w+')

for i in range(0,100):
    f.write(str(random.randint(0,300))+ "\n")

f.close()
f1=open("factorial.txt",'r+')
lines= f1.readlines()
for line in lines:
    print(line)
    print("Facorial of given Number is:" + str(math.factorial(int(line))) + '\n')

