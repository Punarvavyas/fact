import math
import fileinput
import random


f= open("fibonacci.txt",'w+')

for i in range(0,100):
    f.write(str(random.randint(0,100))+ "\n")

f.close()

f1=open("fibonacci.txt",'r+')
lines= f1.readlines()
for line in lines:
    first=0
    second = 1
    count = 0
    totalterms=int(line)
    if totalterms <= 0:
        print("Enter a positive integer")
    elif totalterms == 1:
        print("Fibonacci sequence of total terms", totalterms, ":")
        print(first)
    else:
        print("Fibonacci sequence of total terms:", totalterms)
        while count < totalterms:
            print(first)
            nth = first + second
            first = second
            second = nth
            count += 1
f1.close()