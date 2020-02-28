import math
import fileinput
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

Nvalue=[]
timevalue=[]
f= open("factorial.txt",'w+')

for i in range(0,100):
    f.write(str(random.randint(0,3000))+ "\n")

f.close()
f1=open("factorial.txt",'r+')
lines= f1.readlines()
counter=1
for line in lines:
    Nvalue.append(counter)
    counter=counter+1
    t1=time.time()
    print(line)
    print("Facorial of given Number is:" + str(math.factorial(int(line))) + '\n')
    t2=time.time()
    t3=t2-t1
    timevalue.append(t3)
for i in range(len(Nvalue)):
    print("Request No:" + str(Nvalue[i]) + ",Time Value:" + str(timevalue[i]))

axs = pd.DataFrame({'N_value': Nvalue, 'Time': timevalue})
axs.plot(x='N_value', y='Time', kind='line',color='yellow')
plt.show()

