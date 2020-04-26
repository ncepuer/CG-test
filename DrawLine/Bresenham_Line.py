import numpy as np
import matplotlib.pyplot as plt

def Bresenham(x0,y0,x1,y1):
    plt.axis([x0,x1,y0,y1])
    plt.title("Bresenham_Line")
    plt.xticks(np.arange(x0,x1+0.1,1))
    plt.yticks(np.arange(y0,y1+0.1,0.5))
    plt.grid()
    plt.plot([x0,x1], [y0,y1], color='b', linewidth=2, linestyle="-")
    dx=x1-x0; dy=y1-y0;
    k=dy/dx; e=-0.5
    print(k)
    x=x0; y=y0
    for i in range(dx+1):
        plt.scatter(x, y, c='g', s=500, marker='.')
        x+=1; e+=k
        if e>=0:
            y+=1
            e-=1
    plt.show()
    return
Bresenham(0,0,16,9)