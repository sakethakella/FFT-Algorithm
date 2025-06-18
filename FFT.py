from re import S
##calculates fft by DIT O(nlogn) complexity

import cmath
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import seaborn as sns

def fft(y):
  n=len(y)
  if (n==1):
     return [y[0]]
  
  elif(n!=1):
    a=y[0::2]
    b=y[1::2]
    even=fft(a)
    odd=fft(b)
    c=[0 for element in even]
    d=[0 for element in odd]
    for i in range(int(n/2)):
      odd[i]=odd[i]*(cmath.exp((-2j*cmath.pi*i)/n))
      c[i]=even[i]+odd[i]
      d[i]=even[i]-odd[i]
    return c+d

#creating an random array of size any power of 
twos_power=2**6
x=np.ones(twos_power,dtype=complex)
for i in range(0,int(len(x))):
  x[i]=10*2.713**(-(i/5))
a=fft(x)
plot_range=range(0,int(len(x)))
plt.figure(figsize=(10,5))
plt.plot(plot_range,x,'o')
plt.plot(plot_range,np.real(a),'o')
plt.title('FFT')
plt.xlabel('Sampled time')
plt.ylabel('FFT value')
plt.grid(True)
plt.show()
