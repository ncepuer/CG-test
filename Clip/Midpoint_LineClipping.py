'''
@Author : Ruocong
@File : Midpoint_LineClipping.py 
@Time : 2020/5/20 22:12 
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


def getpoint(x0, y0, x1, y1, XL, XR, YB, YT):
    code0 = getcode(x0, y0, XL, XR, YB, YT)
    flag = True
    err = 0.01
    if code0 == 0:
        x_ = x0;    y_ = y0
    else:
        code1 = getcode(x1, y1, XL, XR, YB, YT)
        if code0 & code1 == 0:
            while True:
                xm = (x0 + x1) / 2
                ym = (y0 + y1) / 2
                if abs(xm - x1) > err or abs(ym - y1) > err:
                    codem = getcode(xm, ym, XL, XR, YB, YT)
                    if code0 & codem != 0:
                        x0 = xm;    y0 = ym
                        code0 = codem
                    else:
                        x1 = xm;    y1 = ym
                        code1 = codem
                else:
                    x_ = xm;    y_ = ym
                    break
        else:
          flag = False;
    return [x_,y_,flag]


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
plt.title("Midpoint_LineClipping")
plt.xticks(np.arange(xmin - 1, xmax + 1.1, 1))
plt.yticks(np.arange(ymin - 1, ymax + 1.1, 1))
plt.grid()
plt.plot(x, y, color='g', linewidth=2, linestyle="-")
plt.plot([x0, x1], [y0, y1], color='b', linewidth=1, linestyle="-") # 画出原始直线和裁剪窗口

[x0_, y0_, flag] = getpoint(x0, y0, x1, y1, XL, XR, YB, YT)
if flag != False:
    [x1_, y1_, flag] = getpoint(x1, y1, x0, y0, XL, XR, YB, YT)
    plt.plot([x0_, x1_], [y0_, y1_], color='r', LineWidth=2, linestyle="-")

plt.show()
