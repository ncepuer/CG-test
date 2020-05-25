'''
@Author : Ruocong
@File : PolygonClipping.py 
@Time : 2020/5/24 19:21 
'''
import numpy as np
import matplotlib.pyplot as plt
import math


def isInside(x, y, x0, y0, x1, y1):
    if x1 > x0:
        if y >= y0:
            return True
    elif x1 < x0:
        if y <= y0:
            return True
    else:
        if y1 > y0:
            if x <= x0:
                return True
        elif y1 < y0:
            if x >= x0:
                return True
    return False


def getpoint(x, y, xp, yp, x0, y0, x1, y1):
    if y0 == y1:
        yi = y0
        xi = x + (y0 - y) * (xp - x) / (yp - y)
    else:
        xi = x0
        yi = y + (x0 - x) * (yp - y) / (xp - x)
    return [xi, yi]


def PolygonClipping():
    xp = [-2, 0.2, 1.6, -2]
    yp = [0.5, -2, 1.5, 0.5]  # 多边形
    xw = [-1, 1, 1, - 1, - 1];
    yw = [-1, - 1, 1, 1, - 1];  # 裁剪窗口
    xmin = int(min(min(xp), min(xw)))
    xmax = math.ceil(max(max(xp), max(xw)))
    ymin = int(min(min(yp), min(yw)))
    ymax = math.ceil(max(max(yp), max(yw)))
    name = ["PolygonClipping","Bottom","Right","Up","Left"]

    for i in range(1,6,1):
        plt.subplot(2,3,i)
        plt.axis('square')
        plt.title(name[i-1])
        plt.xticks(np.arange(xmin - 1, xmax + 1.1, 1))
        plt.yticks(np.arange(ymin - 1, ymax + 1.1, 1))
        plt.grid()
        plt.plot(xw, yw, color='g', linewidth=2, linestyle="-")
        plt.plot(xp, yp, color='k', linewidth=1, linestyle="-")  # 画出原始多边形和裁剪窗口

    iX = xp
    iY = yp
    color = ['b', 'c', 'm', 'r']
    for i in range(4):
        num = len(iX)
        xs = iX[0]
        ys = iY[0]
        oX = []
        oY = []
        for j in range(1, num, 1):
            xp = iX[j]
            yp = iY[j]
            if isInside(xp, yp, xw[i], yw[i], xw[i + 1], yw[i + 1]):
                if isInside(xs, ys, xw[i], yw[i], xw[i + 1], yw[i + 1]):
                    oX = oX + [xp]
                    oY = oY + [yp]  # 情况（1）
                else:
                    [xi, yi] = getpoint(xs, ys, xp, yp, xw[i], yw[i], xw[i + 1], yw[i + 1])
                    oX = oX + [xi]
                    oY = oY + [yi]
                    oX = oX + [xp]
                    oY = oY + [yp]  # 情况（4）
            else:
                if isInside(xs, ys, xw[i], yw[i], xw[i + 1], yw[i + 1]):
                    [xi, yi] = getpoint(xs, ys, xp, yp, xw[i], yw[i], xw[i + 1], yw[i + 1])
                    oX = oX + [xi]
                    oY = oY + [yi]  # 情况（3）
            xs = xp
            ys = yp
        oX = oX + [oX[0]]
        oY = oY + [oY[0]]
        iX = oX
        iY = oY

        for k in range(i+2,6,1):
            plt.subplot(2,3,k)
            plt.plot(oX, oY, color=color[i], linewidth=2, linestyle="-")  # 画出经一个边界裁剪后的多边形

    plt.show()
    return


PolygonClipping()
