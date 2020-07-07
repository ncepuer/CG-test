'''
@Author : Ruocong
@File : ScanFill_Color.py 
@Time : 2020/7/1 08:43 
'''
import numpy as np
import matplotlib.pyplot as plt
import math

x0 = [9, 1, 14]
y0 = [16, 7, 1]  # 三角形的顶点坐标
r0 = [1, 0.3, 0.6]
g0 = [0.2, 0.4, 0.9]
b0 = [0.1, 0.8, 0.4]  # 三角形顶点对应的RGB颜色值

plt.axis('square')
plt.title('TriangleScan_Color')
plt.xticks(np.arange(min(x0) - 1, max(x0) + 1.1, 1))
plt.yticks(np.arange(min(y0) - 1, max(y0) + 1.1, 1))
plt.grid()
plt.plot(x0 + [x0[0]], y0 + [y0[0]], color=(0, 0, 0), linewidth=1, linestyle="-")
plt.scatter(x0, y0, c=(r0, g0, b0), s=100, marker='.')  # 画出三角形的顶点及边（边默认为黑色）

ar = (y0[1] - y0[0]) * (r0[2] - r0[0]) - (r0[1] - r0[0]) * (y0[2] - y0[0])
br = (x0[2] - x0[0]) * (r0[1] - r0[0]) - (r0[2] - r0[0]) * (x0[1] - x0[0])
cr = (x0[1] - x0[0]) * (y0[2] - y0[0]) - (y0[1] - y0[0]) * (x0[2] - x0[0])
dr = (-1) * (ar * x0[0] + br * y0[0] + cr * r0[0])
ag = (y0[1] - y0[0]) * (g0[2] - g0[0]) - (g0[1] - g0[0]) * (y0[2] - y0[0])
bg = (x0[2] - x0[0]) * (g0[1] - g0[0]) - (g0[2] - g0[0]) * (x0[1] - x0[0])
cg = (x0[1] - x0[0]) * (y0[2] - y0[0]) - (y0[1] - y0[0]) * (x0[2] - x0[0])
dg = (-1) * (ag * x0[0] + bg * y0[0] + cg * g0[0])
ab = (y0[1] - y0[0]) * (b0[2] - b0[0]) - (b0[1] - b0[0]) * (y0[2] - y0[0])
bb = (x0[2] - x0[0]) * (b0[1] - b0[0]) - (b0[2] - b0[0]) * (x0[1] - x0[0])
cb = (x0[1] - x0[0]) * (y0[2] - y0[0]) - (y0[1] - y0[0]) * (x0[2] - x0[0])
db = (-1) * (ab * x0[0] + bb * y0[0] + cb * b0[0])

NET = []
for i in range(max(y0) + 1):
    NET.append([])
    for j in range(len(y0)):
        if y0[j] == i:
            if y0[j - 1] > y0[j]:
                data0 = [x0[j], (x0[j - 1] - x0[j]) / (y0[j - 1] - y0[j]), y0[j - 1]]
                NET[i].append(data0)
            if y0[(j + 1)%len(y0)] > y0[j]:
                data0 = [x0[j], (x0[(j + 1)%len(y0)] - x0[j]) / (y0[(j + 1)%len(y0)] - y0[j]), y0[(j + 1)%len(y0)]]
                NET[i].append(data0)
y = min(y0)
AET = []
for i in range(min(y0), max(y0) + 1):
    for j in range(len(NET[i])):
        AET.append(NET[i][j])
    for j in range(0, len(AET) - 1):  # 排序
        for k in range(0, len(AET) - j - 1):
            if AET[k][0] > AET[k + 1][0]:
                AET[k], AET[k + 1] = AET[k + 1], AET[k]
    for j in range(0, len(AET), 2):
       for k in range(math.ceil(AET[j][0]), int(AET[j+1][0])+1):
          r = (-1) * (ar / cr) * k + (-1) * (br / cr) * i + (-1) * (dr / cr)
          g = (-1) * (ag / cg) * k + (-1) * (bg / cg) * i + (-1) * (dg / cg)
          b = (-1) * (ab / cb) * k + (-1) * (bb / cb) * i + (-1) * (db / cb)
          plt.scatter(k, i, c=[(r, g, b)], s=100, marker='.')
    j = 0
    while j < len(AET):
        if i + 1 < max(y0):
            NextScanLine = i + 1;
        else:
            NextScanLine = i;
        if AET[j][2] == NextScanLine:
            AET.pop(j)
        if j<len(AET):
            if AET[j][2] > NextScanLine:
                AET[j][0] += AET[j][1]
        j += 1

plt.show()
