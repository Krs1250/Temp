from cgi import print_arguments
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def knn_iris():
    """
    用KNN算法对鸢尾花进行分类
    :return:
    """
    # 1) 获取数据
    iris = load_iris()

    # 2) 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=6)
    
    # 3) 特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    
    # 4) KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors = 3)
    estimator.fit(x_train,y_train)
    
    # 5) 模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n",y_predict)
    print("直接比对真实值和预测值:\n",y_test == y_predict)

    # 方法2：计算准确值
    score = estimator.score(x_test,y_test)
    print(x_test,y_test)
    print(score)
    return None

def knn_iris_gscv():
    """
    用KNN算法对鸢尾花进行分类,使用网格搜索
    :return:
    """
    # 1) 获取数据
    iris = load_iris()

    # 2) 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,random_state=6)
    
    # 3) 特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    
    # 4) KNN算法预估器

    estimator = KNeighborsClassifier(n_neighbors = 3)
    # 参数准备
    param = {"n_neighbors": [3, 5, 10]}
    estimator = GridSearchCV(estimator,param_grid=param,cv = 2)
    estimator.fit(x_train,y_train)
    
    # 5) 模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n",y_predict)
    print("直接比对真实值和预测值:\n",y_test == y_predict)

    # 方法2：计算准确值
    score = estimator.score(x_test,y_test)
    print(x_test,y_test)
    print(score)

    # bestscore:在交叉验证中验证的最好结果_
    # bestestimator：最好的参数模型
    # cvresults:每次交叉验证后的验证集准确率结果和训练集准确率结果
    print("验证的最好结果：\n", estimator.best_score_)
    print("最好的参数模型：\n", estimator.best_estimator_)
    print("每次交叉验证结果：\n", estimator.cv_results_) #交叉验证实际上就是自身
    return None

if __name__ == "__main__":
    # 代码1：用KNN算法对鸢尾花进行分类
    # knn_iris()
    # 代码1：用KNN算法对鸢尾花进行分类，使用网格搜索
    knn_iris_gscv()