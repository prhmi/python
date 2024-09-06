import pandas as pn
import numpy as np
from matplotlib import pyplot as plt



def plot(filename,colorme,mode):
    with open(filename, 'r') as f:
        data = f.read()
        res = [float(i) for i in data.split()]
    iLen =  len(res)
    indxx = 0
    x = []
    while indxx < iLen:
        x = x + [res[indxx]]
        indxx += 2
    # print(x)
    indxy = 1
    y = []
    while indxy < iLen:
        y = y + [res[indxy]]
        indxy += 2
    if mode == 1:
        plt.step(y,x,color= colorme)
    elif mode == 2:
        plt.scatter(y,x,color= colorme)
    elif mode == 3:
        plt.step(y,x,color= colorme)
filename1 = "FrqLine1.txt"
filename2 = "FrqLine2.txt"
filename3 = "FrqLine3.txt"
filename4 = "ShortNotes.txt"

filename5 = "shahed1.txt"
filename6 = "Ist1.txt"
filename7 = "shahed2.txt"
filename8 = "Ist2.txt"
filename9 = "shahed3.txt"
filename10 = "Ist3.txt"


plt.figure(figsize=(12,6))
plot(filename1, (0.2, 0.5, 0.7),1)
plot(filename4, (0.3, 0.5, 0.7),2)

plot(filename5, (0.8, 0, 0, 0.4),3)
plot(filename6, (0.2, 0.5, 0, 0.4),3)

plot(filename2, (0.2, 0.5, 0.7),1)
plot(filename3, (0.2, 0.5, 0.7),1)
plot(filename7, (0.8, 0, 0, 0.4),3)
plot(filename8, (0.2, 0.5, 0, 0.4),3)
plot(filename9, (0.8, 0, 0, 0.4),3)
plot(filename10, (0.2, 0.5, 0, 0.4),3)

plt.title('Music for Black Sine Wave | B = 60.61 Hz ')
plt.xlabel('time (sec)')
plt.ylabel('Frq (Hz)')
plt.legend(['Long Notes', 'Short Notes','Base Frq','ist'])
plt.grid(True,color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()
