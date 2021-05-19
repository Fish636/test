# 导入库
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3 * np.pi, 100) #将[0，3π]进行100等分
y = np.sin(x) # y=sin（x）

plt.rcParams['font.sans-serif']=['SimHei'] #在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(121) #将图片显示到第一行第一列
plt.title(r'$f(x)=sin(x)$') #显示图片标题
plt.plot(x, y)#显示连续信号

x1=[t*0.375*np.pi for t in x] #将t转变带换成x赋值给x1
y1=np.sin(x1)
plt.subplot(122) #将图片显示到第一行第二列
plt.title(r'$f(x)=sin(\omega x),\omega=\frac{3}{8}\pi$') #显示标题
plt.plot(x,y1) #显示连续信号

plt.show() #图片显示

