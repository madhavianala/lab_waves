import numpy as np
import matplotlib.pyplot as mp
f1=int(input("enter fist wave freq.="))
f2=int(input("enter second wave freq.="))
fs=int(input("enter third wave freq.="))
n=int(input("enter no.of samples="))
t=np.arange(n)
x1=np.cos(2*np.pi*t*f1/fs)
mp.subplot(3,1,1)
mp.plot(t,x1)
mp.title("cos wave")
mp.xlabel("time")
mp.ylabel("amplitude")
x2=np.sin(2*np.pi*t*f2/fs)
mp.subplot(3,1,2)
mp.plot(t,x2)
mp.title("sin wave")
mp.xlabel("time")
mp.ylabel("amplitude")
x=x1+x2
mp.subplot(3,1,3)
mp.plot(t,x)
mp.title("resultant wave")
mp.xlabel("time")
mp.ylabel("amplitude")
mp.show( )




output:
f1=50
f2=75
fs=1000
n=100