'''
@Author : Ruocong
@File : ScanFill_Color_Improved.py 
@Time : 2020/7/3 15:33 
'''
import numpy as np
import matplotlib.pyplot as plt
import math


def adjust_rgb(x):  # 规定RGB值范围[0,1]
    if x > 1:
        x = 1
    elif x < 0:
        x = 0
    return x


def FillTriangle(x0, y0, rgb0):
    a = [0 for x in range(3)]
    b = [0 for x in range(3)]
    c = [0 for x in range(3)]
    d = [0 for x in range(3)]
    for i in range(3):
        a[i] = (y0[1] - y0[0]) * (rgb0[i][2] - rgb0[i][0]) - (rgb0[i][1] - rgb0[i][0]) * (y0[2] - y0[0])
        b[i] = (x0[2] - x0[0]) * (rgb0[i][1] - rgb0[i][0]) - (rgb0[i][2] - rgb0[i][0]) * (x0[1] - x0[0])
        c[i] = (x0[1] - x0[0]) * (y0[2] - y0[0]) - (y0[1] - y0[0]) * (x0[2] - x0[0])
        d[i] = (-1) * (a[i] * x0[0] + b[i] * y0[0] + c[i] * rgb0[i][0])  # 由算法得出a,b,c,d各参数的值
    NET = []  # 创建新边表
    for i in range(max(y0) + 1):
        NET.append([])
        for j in range(len(y0)):
            if y0[j] == i:
                if y0[j - 1] > y0[j]:
                    data0 = [x0[j], (x0[j - 1] - x0[j]) / (y0[j - 1] - y0[j]), y0[j - 1]]
                    NET[i].append(data0)
                if y0[(j + 1) % len(y0)] > y0[j]:
                    data0 = [x0[j], (x0[(j + 1) % len(y0)] - x0[j]) / (y0[(j + 1) % len(y0)] - y0[j]),
                             y0[(j + 1) % len(y0)]]
                    NET[i].append(data0)
    y = min(y0)
    AET = []  # 创建活性边表
    for i in range(min(y0), max(y0) + 1):
        for j in range(len(NET[i])):
            AET.append(NET[i][j])
        for j in range(0, len(AET) - 1):  # 排序
            for k in range(0, len(AET) - j - 1):
                if AET[k][0] > AET[k + 1][0]:
                    AET[k], AET[k + 1] = AET[k + 1], AET[k]
        for j in range(0, len(AET), 2):
            for k in range(math.ceil(AET[j][0]), int(AET[j + 1][0]) + 1):
                rx = adjust_rgb((-1) * (a[0] / c[0]) * k + (-1) * (b[0] / c[0]) * i + (-1) * (d[0] / c[0]))
                gx = adjust_rgb((-1) * (a[1] / c[1]) * k + (-1) * (b[1] / c[1]) * i + (-1) * (d[1] / c[1]))
                bx = adjust_rgb((-1) * (a[2] / c[2]) * k + (-1) * (b[2] / c[2]) * i + (-1) * (d[2] / c[2]))
                plt.scatter(k, i, c=[[rx, gx, bx]], s=100, marker='.')  # 根据a,b,c,d参数确定各点的RGB值
        j = 0
        while j < len(AET):
            if i + 1 < max(y0):
                NextScanLine = i + 1
            else:
                NextScanLine = i
            if AET[j][2] == NextScanLine:
                AET.pop(j)
            if j < len(AET):
                if AET[j][2] > NextScanLine:
                    AET[j][0] += AET[j][1]
            j += 1
    return


x0 = [1, 2, 4, 9, 13, 15, 14, 9, 4]
y0 = [7, 12, 15, 16, 13, 6, 2, 1, 2]  # 凸多边形的顶点坐标
r0 = [1, 0.6, 0.3, 0.6, 0.5, 0.9, 0.1, 0.4, 0.8]
g0 = [0.2, 0.4, 0.9, 1, 0.6, 0.5, 0.1, 0.8, 0.3]
b0 = [0.1, 0.8, 0.4, 0.5, 0.8, 1, 0.9, 0.2, 0.4]  # 凸多边形顶点对应的RGB颜色值
rgb0 = []
for i in range(len(r0)):
    rgb0.append([r0[i], g0[i], b0[i]])

plt.axis('square')
plt.title('PolygonScan_Color')
plt.xticks(np.arange(min(x0) - 1, max(x0) + 1.1, 1))
plt.yticks(np.arange(min(y0) - 1, max(y0) + 1.1, 1))
plt.grid()
plt.plot(x0 + [x0[0]], y0 + [y0[0]], color=(0, 0, 0), linewidth=1, linestyle="-")
plt.scatter(x0, y0, c=rgb0, s=100, marker='.')  # 画出凸多边形的顶点及边（边默认为黑色）

for i in range(len(x0) - 2):  # 将凸多边形分解为多个三角形，再利用三角形的颜色渐变扫描填充算法进行填充
    x = [x0[0], x0[i + 1], x0[i + 2]]
    y = [y0[0], y0[i + 1], y0[i + 2]]
    rgb = [[r0[0], r0[i + 1], r0[i + 2]], [g0[0], g0[i + 1], g0[i + 2]], [b0[0], b0[i + 1], b0[i + 2]]]
    FillTriangle(x, y, rgb)

plt.show()
