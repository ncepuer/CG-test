import numpy as np
import matplotlib.pyplot as plt

def Midpoint_Circle(r):
    plt.axis('square')
    plt.title("Midpoint_Circle")
    plt.xticks(np.arange(-r-1,r+1.1,1))
    plt.yticks(np.arange(-r-1,r+1.1,1))
    plt.grid()
    theta=np.arange(0,2*np.pi,0.01)
    x0=r*np.cos(theta)
    y0=r*np.sin(theta)
    plt.plot(x0, y0, color='b', linewidth=2, linestyle="-")
    plt.scatter(0, 0, c='r', s=300, marker='.')
    x=r; y=0; d=1.25-r
    xa=[]; ya=[]
    while y<=x:
        xa.append(x); ya.append(y)
        if d<0: d+=2*y+3
        else: d+=2*(y-x)+5; x-=1
        y+=1
    for i in range(len(xa) - 1,-1,-1):
        x=ya[i]; y=xa[i]
        xa.append(x); ya.append(y)
    for i in range(len(xa) - 1, -1, -1):
        x=-xa[i]; y=ya[i]
        xa.append(x); ya.append(y)
    for i in range(len(xa) - 1, -1, -1):
        x=xa[i]; y=-ya[i]
        xa.append(x); ya.append(y)
    for i in range(0,len(xa)):
        plt.scatter(xa[i], ya[i], c='g', s=100, marker='.')
    plt.show()
    return

Midpoint_Circle(10)