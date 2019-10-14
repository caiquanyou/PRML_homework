import numpy as np
import matplotlib.pyplot as plt

#输入w1,w2两类模式
w1 = np.array([[0, 2, 2,0], [0, 0, 2, 2]], dtype=np.float64)
w2 = np.array([[4, 6, 6, 4], [4, 4, 6, 6]], dtype=np.float64)
w1_t = np.matrix(w1)
w1_cov = np.matrix(np.cov(w1_t))
w1_cov_I = w1_cov.I
print(w1_cov_I)
#w1的均值向量
m1 = np.matrix(np.array([[1],[1]], dtype=np.float64))
w2_t = np.matrix(w2)
w2_cov = np.matrix(np.cov(w2_t))
w2_cov_I = w2_cov.I
print(w2_cov_I)
#w2的均指向量
m2 = np.matrix(np.array([[5],[5]], dtype=np.float64))
M = (m1 -m2).T*w1_cov_I
N = -1/2*m1.T*w1_cov_I*m1+1/2*m2.T*w2_cov_I*m2
print(N)
print("判别界面方程为：%f x1 + %f x2 +%f = 0" % (M[0, 0].T, M[0, 1],N))


# 绘图
x = np.arange(-60, 60, .01)
y = np.arange(-60, 60, .01)
x, y = np.meshgrid(x, y)
# 绘制分界线
F = (M[0, 0])*x + (M[0, 1])*y + N

# 作图
plt.figure()
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('判别界面')
plt.contour(x, y, F, 0, colors='black')
plt.show()
