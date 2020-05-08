import numpy as np
import matplotlib.pyplot as plt
import math

def PolygonFill():
    plt.axis('square')
    plt.title("PolygonScanLine")
    x0 = [3, 5, 5, 8, 10, 7, 5, 5, 1, 2, 1, 3, 3];
    y0 = [1, 1, 4, 4, 6, 8, 8, 7, 7, 5, 3, 3, 1];
    plt.xticks(np.arange(min(x0) - 1, max(x0) + 1.1, 1))
    plt.yticks(np.arange(min(y0) - 1, max(y0) + 1.1, 1))
    plt.grid()
    plt.plot(x0, y0, color='b', linewidth=2, linestyle="-")
    x0.pop(-1)
    y0.pop(-1)
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
              plt.scatter(k, i, c='g', s=100, marker='.')
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
    return


PolygonFill()
