import numpy as np
import matplotlib.pyplot as plt

def Midpoint_Line(x0, y0, x1, y1):
    plt.axis('square')
    plt.title("Midpoint_Line")
    plt.xticks(np.arange(x0,x1+0.1,1))
    plt.yticks(np.arange(y0,y1+0.1,0.5))
    plt.grid()
    plt.plot([x0,x1], [y0,y1], color='b', linewidth=2, linestyle="-")
    a=y0-y1; b=x1-x0; d=2*a+b
    d1=2*a; d2=(a+b)*2
    x=x0;y=y0
    while x <= x1:
        plt.scatter(x, y, c='g', s=500, marker='.')
        if d<0:
            x+=1; y+=1; d+=d2
        else:
            x+=1; d+=d1
    plt.show()
    return

Midpoint_Line(0, 0, 16, 9)