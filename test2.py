import numpy as np
import matplotlib.pyplot as plt

#实现了用鼠标任意输入特征多边形的顶点，但是能力有限，没有实现橡皮筋效果
class Bezier:     #定义Bezier类
    def __init__(self, line):
        self.xs = list()  # 保存点的x坐标
        self.ys = list()  # 保存点的y坐标
        self.line = line
        self.press = 0  # 1为按下，0为没按下
        self.cidpress = line.figure.canvas.mpl_connect('button_press_event', self.on_press)  # 鼠标按下事件
        self.cidrelease = line.figure.canvas.mpl_connect('button_release_event', self.on_release)  # 鼠标放开事件


    def on_release(self, event):  # 鼠标释放
        if event.inaxes != self.line.axes:
            return
        self.xs.append(event.xdata)     #根据鼠标点击位置添加点
        self.ys.append(event.ydata)
        self.draw()    #画图
        self.press = 0    #恢复

    def on_press(self, event):  # 鼠标按下
        if event.inaxes != self.line.axes:
            return
        self.press = 1

    def draw(self):  #画曲线
        self.line.clear()  #清除重新画
        self.line.axis([0, 1, 0, 1])
        self.bezier(self.xs, self.ys)  #Bezier曲线
        self.line.scatter(self.xs, self.ys, color='r', s=200, marker=".")#画点
        self.line.plot(self.xs, self.ys, color='r') #画线
        self.line.figure.canvas.draw()

    def bezier(self, *s):  #de Casteljau递推算法
        n = len(s[0])  #所画点的个数
        x, y = [], []
        x1, y1 = [], []
        index = 0
        for k in np.linspace(0, 1):   #01之间
            for i in range(1, n):
                for j in range(0, n - i):
                    if i == 1:
                        x1.insert(j, s[0][j] * (1 - k) + s[0][j + 1] * k)
                        y1.insert(j, s[1][j] * (1 - k) + s[1][j + 1] * k)
                        continue
                    # i != 1
                    x1[j] = x1[j] * (1 - k) + x1[j + 1] * k
                    y1[j] = y1[j] * (1 - k) + y1[j + 1] * k
            if n == 1:
                x.insert(index, s[0][0])
                y.insert(index, s[1][0])
            else:
                x.insert(index, x1[0])
                y.insert(index, y1[0])
                x1 = []
                y1 = []
            index = index + 1
        self.line.plot(x, y)

if __name__=='__main__':
    fig = plt.figure(1, figsize=(18, 9))
    ax = fig.add_subplot(111)
    ax.set_title('Bezier Curves')
    myBezier = Bezier(ax)
    plt.show()