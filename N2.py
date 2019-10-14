W = [1,1, 0, 0]
w1 = [[1, 1, 0, 1], [0, 0, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]]
w2 = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [0, 0, 1, 1]]
flag = False
while flag != True:
    for i in range(len(w1)):
            t1 = 0
            t2 = 0
            for j in range(len(W)):
                t1 += W[j] * w1[i][j]
                t2 += W[j] * w2[i][j]
            if (t1 <= 0):
                for j in range(len(W)):
                    W[j] += w1[i][j]
                flag = False
                break
            if (t2 >= 0):
                for j in range(len(W)):
                    W[j] -= w2[i][j]
                flag = False
                break
            flag = True
print("判别函数：" + "d(x)= %d" % (W[0]) + "x1" + "%d" % (W[1]) + "x2" + "%d" % (W[2]) + "x3+" + "%d" % (W[3]))
