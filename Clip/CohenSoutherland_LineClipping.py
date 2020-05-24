'''
@Author : Ruocong
@File : CohenSoutherland_LineClipping.py 
@Time : 2020/5/20 20:23 
'''
import numpy as np
import matplotlib.pyplot as plt


def getcode(x, y, XL, XR, YB, YT):
    code = 0
    if x < XL:
        code = code | 0b0001
    if x > XR:
        code = code | 0b0010
    if y < YB:
        code = code | 0b0100
    if y > YT:
        code = code | 0b1000
    return code


def CohenSoutherland_LineClipping():
    x0 = 3
    y0 = 1
    x1 = 13
    y1 = 8  # 线段
    x = [4, 11, 11, 4, 4]
    y = [2, 2, 7, 7, 2]  # 裁剪窗口
    XL = min(x)
    XR = max(x)
    YB = min(y)
    YT = max(y)
    xmin = min([XL, min([x0, x1])])
    xmax = max(XR, max(x0, x1))
    ymin = min([YB, min([y0, y1])])
    ymax = max(YT, max(y0, y1))

    plt.axis([xmin, xmax, ymin, ymax], 'square')
    plt.title("CohenSoutherland_LineClipping")
    plt.xticks(np.arange(xmin - 1, xmax + 1.1, 1))
    plt.yticks(np.arange(ymin - 1, ymax + 1.1, 1))
    plt.grid()
    plt.plot(x, y, color='g', linewidth=2, linestyle="-")
    plt.plot([x0, x1], [y0, y1], color='b', linewidth=1, linestyle="-") # 画出原始直线和裁剪窗口

    code0 = getcode(x0, y0, XL, XR, YB, YT)
    code1 = getcode(x1, y1, XL, XR, YB, YT)
    flag = True
    while code0 != 0 or code1 != 0:
        if code0 & code1 != 0:
            flag = False
            break
        if code0 != 0:
            code = code0
        else:
            code = code1
        if 0b0001 & code != 0:
            x = XL
            y = y0 + (y1 - y0) * (XL - x0) / (x1 - x0)
        elif 0b0010 & code != 0:
            x = XR
            y = y0 + (y1 - y0) * (XR - x0) / (x1 - x0)
        elif 0b0100 & code != 0:
            y = YB
            x = x0 + (x1 - x0) * (YB - y0) / (y1 - y0)
        elif 0b1000 & code != 0:
            y = YT
            x = x0 + (x1 - x0) * (YT - y0) / (y1 - y0)
        if code == code0:
            x0 = x
            y0 = y
            code0 = getcode(x, y, XL, XR, YB, YT)
        else:
            x1 = x
            y1 = y
            code1 = getcode(x, y, XL, XR, YB, YT)
    if flag == True:
        plt.plot([x0, x1], [y0, y1], color='r', linewidth=2, linestyle="-")

    plt.show()
    return


CohenSoutherland_LineClipping()
