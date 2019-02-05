import numpy as np
import matplotlib.pyplot as mp
t=np.arange(0,20,0.1)
x1=np.cos(t)
mp.subplot(1,3,1)
mp.plot(t,x1)
mp.title("cos wave")
mp.xlabel("time")
mp.ylabel("amplitude")
t=np.arange(0,20,0.1)
x2=np.sin(t)
mp.subplot(1,3,2)
mp.plot(t,x2)
mp.title("sin wave")
mp.xlabel("time")
mp.ylabel("amplitude")
x=x1+x2
mp.subplot(1,3,3)
mp.plot(t,x)
mp.title("resultant wave")
mp.xlabel("time")
mp.ylabel("amplitude")
mp.show( )
