'''
@Author : Ruocong
@File : LiangBarskey_LineClipping.py 
@Time : 2020/5/21 9:54 
'''
import numpy as np
import matplotlib.pyplot as plt


def getU(p, q, u0, u1):
    flag = True
    if p < 0:
        r = q / p
        if r > u1:
            flag = False
        elif r > u0:
            u0 = r
            flag = True
    elif p > 0:
        r = q / p
        if r < u0:
            flag = False
        elif r < u1:
            u1 = r
    else:
        if q < 0:
            flag = False
    return [u0, u1, flag]


def LB_LineClipping():
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
    plt.title("LiangBarskey_LineClipping")
    plt.xticks(np.arange(xmin - 1, xmax + 1.1, 1))
    plt.yticks(np.arange(ymin - 1, ymax + 1.1, 1))
    plt.grid()
    plt.plot(x, y, color='g', linewidth=2, linestyle="-")
    plt.plot([x0, x1], [y0, y1], color='b', linewidth=1, linestyle="-")  # 画出原始直线和裁剪窗口

    u0 = 0;    u1 = 1
    dx = x1 - x0;    dy = y1 - y0
    [u0, u1, flag] = getU(-dx, x0 - XL, u0, u1)  # get U_Left
    if flag:
        [u0, u1, flag] = getU(dx, XR - x0, u0, u1)  # get U_Right
        if flag:
            [u0, u1, flag] = getU(-dy, y0 - YB, u0, u1)  # get U_Bottom
            if flag:
                [u0, u1, flag] = getU(dy, YT - y0, u0, u1)  # get U_Top
                if flag:
                    plt.plot([x0 + u0 * dx, x0 + u1 * dx], [y0 + u0 * dy, y0 + u1 * dy], color='r', linewidth=2, linestyle='-')

    plt.show()
    return


LB_LineClipping()
