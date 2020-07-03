'''
@Author : Ruocong
@File : test1.py 
@Time : 2020/7/3 21:05 
'''
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
# ax.plot(np.random.rand(10))

plt.axis('square')
plt.title('Bezier')
plt.xticks(np.arange(-10, 10.1, 1))
plt.yticks(np.arange(-10, 10.1, 1))
plt.grid()
x = [1, 4, 7, 8]
y = [3, 2, 6, 1]
ax.plot(x, y, color='r', linewidth=1, linestyle="-")

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
