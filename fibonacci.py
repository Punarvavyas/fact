import math
import fileinput
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

Nvalue=[]
timevalue=[]
f= open("fibonacci.txt",'w+')

for i in range(0,100):
    f.write(str(random.randint(0,300))+ "\n")

f.close()

f1=open("fibonacci.txt",'r+')
lines= f1.readlines()
reqcount=1
for line in lines:
    t1=time.time()
    Nvalue.append(reqcount)
    reqcount=reqcount+1
    first=0
    second = 1
    count = 0
    totalterms=int(line)
    if totalterms <= 0:
        print("Result")
        print("Enter a positive integer")
    elif totalterms == 1:
        print("Result")
        print("Fibonacci sequence of total terms", totalterms, ":")
        print(first)
    else:
        print("Fibonacci sequence of total terms:", totalterms)
        while count < totalterms:

            print(str(first))
            nth = first + second
            first = second
            second = nth
            count += 1
    t2=time.time()
    t3=t2-t1
    timevalue.append(t3)

f1.close()

for i in range(len(Nvalue)):
    print("Request No:" + str(Nvalue[i]) + ",Time Value:" + str(timevalue[i]))

axs = pd.DataFrame({'N_value': Nvalue, 'Time': timevalue})
axs.plot(x='N_value', y='Time', kind='line',color='yellow')
plt.show()
