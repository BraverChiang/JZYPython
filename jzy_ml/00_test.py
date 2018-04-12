### 01.
from sklearn import tree

# Many types of classifiers
# . Artificial neural network
# . Support Vector Machine
# . Lions
# . Tigers
# . Bears
# . Oh my!

# 000 训练数据
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

# 111 做一个大脑
clf = tree.DecisionTreeClassifier()
# 222 训练这个大脑
clf = clf.fit(features, labels)


# 333 用全新的数据, 测试大脑的训练结果
print(clf.predict([[150, 0]]))

### 02.
from sklearn.datasets import  load_iris
import  numpy as np

# 000 导入网络存在的数据
iris = load_iris()
test_idx = [0, 50, 100]   #这些记录是用来测试的
print(iris.feature_names) # 字段名
print(iris.target_names) # 结果的类型
print(iris.data[0]) # 第一行记录
print(iris.target[0]) # 第一行记录对应的结果

# 000 training data 训练数据(包括: 输入数据, 输出数据)
train_data = np.delete(iris.data, test_idx, axis=0) #总输入数据删掉测试输入数据, 得到训练需要的输入数据
train_target = np.delete(iris.target, test_idx) #总输出数据删掉测试输出数据, 得到训练需要的输出数据

# 000 testing data 测试数据(包括: 输入数据, 输出数据)
test_data = iris.data[test_idx]
test_target = iris.target[test_idx]

# 111 做出大脑, 222 并训练数据进行训练
clf2 = tree.DecisionTreeClassifier()
clf2.fit(train_data, train_target)

# 333 测试test
print(test_target) #直接打印:原本正确的测试结果
print(clf2.predict(test_data)) #打印: 通过机器学习预测出来的结果.

### 03 dogs.
# import  matplotlib.pyplot as plt
#
# grs = 500
# las = 500
# grs_height = 28 + 4 * np.random.randn(grs)
# las_height = 28 + 4 * np.random.randn(las)
#
# plt.hist([grs_height, las_height], stacked=True, color=["r", "b"])
# plt.show()

### 04 原有的大脑 . 05 换个大脑 .
# 06 自制大脑.
# 步骤:
# 1 注释掉原有大脑.
# 2 Implement a class.
# 3 Understand interface.
# 4 Get pipeline working.  运行得到 0.33334
# 5 Intro to k-NN
# 6 Measure distance.
# 7 Implement nearest neighbor algorithm.
# 8 Run pipeline.   运行得到 0.96

import  random
from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)

# 111a 自制大脑
class ScrappyKNN():
    # 大脑训练 简单的模型就是: data直接变成了大脑的w,b参数.
    #  3blue1brown中 cost function.
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # 大脑预测
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            # label = random.choice(self.y_train)
            label = self.closest(row)
            predictions.append(label)
        return predictions

    # 111b 大脑的核心逻辑
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

# 000 导入数据
X = iris.data
y = iris.target

# 000 数据分组
from  sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .5)

# 111 选用一款不同的大脑, 222 大脑训练
#
# my_classifier = tree.DecisionTreeClassifier()
# from  sklearn.neighbors import KNeighborsClassifier
# my_classifier = KNeighborsClassifier()
my_classifier = ScrappyKNN()
my_classifier.fit(X_train, y_train)

# 333 测试结果集
predictions = my_classifier.predict(X_test)

from  sklearn.metrics import  accuracy_score
print(accuracy_score(y_test, predictions))