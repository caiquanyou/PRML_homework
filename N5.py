from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
x_train = [[6], [8], [10], [14], [18]]
y_train = [[7], [9], [13], [17.5], [18]]
# 一次线性回归的学习与预测
# 线性回归模型 学习
regressor = LinearRegression()
regressor.fit(x_train, y_train)
# 画出一次线性回归的拟合曲线
xx = np.linspace(0, 25, 100)   # 0到25均匀采集100个点做x轴
xx = xx.reshape(xx.shape[0], 1)
yy = regressor.predict(xx)  # 计算每个点对应的y
plt.scatter(x_train, y_train)   # 画出训练数据的点
plt1, = plt.plot(xx, yy, label="degree=1")  #绘制数据（plt1,是为了便于后面使用legend添加的，注意，必须添加逗号。
plt.xlim(0,25)
plt.ylim(0,25)
plt.xlabel("Diameter")
plt.ylabel("Price")
plt.legend(handles=[plt1])
plt.show()
# 2次线性回归进行预测
poly2 = PolynomialFeatures(degree=2)    # 2次多项式特征生成器
x_train_poly2 = poly2.fit_transform(x_train)
# 建立模型预测
regressor_poly2 = LinearRegression()
regressor_poly2.fit(x_train_poly2, y_train)
# 画出2次线性回归的图
xx_poly2 = poly2.transform(xx)
yy_poly2 = regressor_poly2.predict(xx_poly2)
plt.scatter(x_train, y_train)
plt1, = plt.plot(xx, yy, label="Degree1")
plt2, = plt.plot(xx, yy_poly2, label="Degree2")
plt.axis([0, 25, 0, 25])
plt.xlabel("Diameter")
plt.ylabel("Price")
plt.legend(handles=[plt1, plt2])
plt.show()
# 输出二次回归模型的预测样本评分
print("二次线性模型在训练数据上得分:", regressor_poly2.score(x_train_poly2, y_train))     # 0.9816421639597427
# 进行四次线性回归模型拟合
poly4 = PolynomialFeatures(degree=4)    # 4次多项式特征生成器
x_train_poly4 = poly4.fit_transform(x_train)
# 建立模型预测
regressor_poly4 = LinearRegression()
regressor_poly4.fit(x_train_poly4, y_train)
# 画出2次线性回归的图
xx_poly4 = poly4.transform(xx)
yy_poly4 = regressor_poly4.predict(xx_poly4)
plt.scatter(x_train, y_train)
plt1, = plt.plot(xx, yy, label="Degree1")
plt2, = plt.plot(xx, yy_poly2, label="Degree2")
plt4, = plt.plot(xx, yy_poly4, label="Degree2")
plt.axis([0, 25, 0, 25])
plt.xlabel("Diameter")
plt.ylabel("Price")
plt.legend(handles=[plt1, plt2, plt4])
plt.show()
# 输出二次回归模型的预测样本评分
print("四次线性训练数据上得分:", regressor_poly4.score(x_train_poly4, y_train))     # 1.0
# 准备测试数据
x_test = [[6], [8], [11], [16]]
y_test = [[8], [12], [15], [18]]
print("一次线性模型在测试集合上得分:", regressor.score(x_test, y_test))   # 0.809726797707665
x_test_poly2 = poly2.transform(x_test)
print("二次线性模型在测试集合上得分:", regressor_poly2.score(x_test_poly2, y_test))   # 0.8675443656345054
x_test_poly4 = poly4.transform(x_test)
print("四次线性模型在测试集合上得分:", regressor_poly4.score(x_test_poly4, y_test))   # 0.8095880795746723