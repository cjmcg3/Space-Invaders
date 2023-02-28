import sys
from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt


data=np.loadtxt(sys.argv[1])

stack_array=np.loadtxt(sys.argv[1],usecols=(0,1,2,3))
#print(stack_array)

ay=stack_array[:,0]
gy=stack_array[:,1]
by=stack_array[:,2]
my=stack_array[:,3]
#print(ay)

print(ay)
#need all the xy points which it will plot
#makes the graph window 
#x=np.linspace(1,len(data),100)
plt.plot(ay,'-r',marker='^',label='red')
plt.plot(gy,'-g',marker='^',label='green')
plt.plot(by,'-b',marker='*',label='blue')
plt.plot(my,'-p',marker='P',label='mine')
plt.ylabel('# Aliens shot')
plt.xlabel('Time steps')
plt.title(str(sys.argv[1])+'Statistics on Alien Killings')
plt.legend(loc='upper left')
plt.show()