import time
import numpy as np
import matplotlib.pyplot as plt

def DDA(x0,y0,x1,y1):
    plt.axis([x0,x1,y0,y1])
    plt.xticks(np.arange(x0,x1+0.1,1))
    plt.yticks(np.arange(y0,y1+0.1,0.5))
    plt.grid()
    plt.plot([x0,x1], [y0,y1], color='b', linewidth=2, linestyle="-")
    dx=x1-x0; dy=y1-y0
    k=dy/dx;
    x=x0; y=y0;
    while x <= x1:
        plt.scatter(x, int(y+0.5), c='g', s=500, marker='.')
        x=x+1; y=y+k
    plt.show()
    return
DDA(0,0,16,9)