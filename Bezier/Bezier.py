'''
@Author : Ruocong
@File : Bezier.py
@Time : 2020/6/25 19:18
'''
# 已实现 用鼠标任意输入特征多边形的顶点
# 未实现 橡皮筋效果
import numpy as np
import matplotlib.pyplot as plt


def getpoint(x, y, t):  # 获取对应t值的Bezier曲线上的点的坐标
    xr = []
    yr = []
    plen = len(x)
    if plen == 1:
        return [x, y]
    else:
        for i in range(plen - 1):
            xr0 = t * x[i + 1] + (1 - t) * x[i]
            yr0 = t * y[i + 1] + (1 - t) * y[i]
            xr.append(xr0)
            yr.append(yr0)
        if t == 0.6:  # 展示t=0.6时的Bezier曲线构造过程
            plt.plot(xr, yr, color='g', linewidth=1, linestyle="-")
            plt.scatter(xr, yr, c='g', s=50, marker='.')
        return getpoint(xr, yr, t)


def draw_Bezier(x, y):
    plt.plot(x, y, color='k', linewidth=1, linestyle="-")
    plt.scatter(x, y, c='k', s=50, marker='.')
    xb = []
    yb = []
    for t in np.arange(0, 1, 0.01):
        [xb0, yb0] = getpoint(x, y, t)
        xb.append(xb0)
        yb.append(yb0)
    xb.append([x[-1]])
    yb.append([y[-1]])
    plt.plot(xb, yb, color='r', linewidth=1, linestyle="-")
    plt.show()


def init(): # 画布初始化
    plt.clf()
    plt.axis('square')
    plt.title('Bezier')
    plt.xticks(np.arange(-10, 10.1, 1))
    plt.yticks(np.arange(-10, 10.1, 1))


def onclick(event):  # 鼠标点击事件响应
    init()
    x.append(event.xdata)
    y.append(event.ydata)
    draw_Bezier(x, y)
    fig.canvas.draw()


x = []
y = []
fig, ax = plt.subplots()
init()
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
