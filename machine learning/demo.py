from turtle import shape
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba
from torch import _fake_quantize_per_tensor_affine_cachemask_tensor_qparams

def dataset_demo():
    """
    sklearn数据集使用
    :return:
    """
    #获取数据集
    iris = load_iris()
    print("鸢尾花数据集：\n",iris)
    print("查看数据集描述：\n",iris["DESCR"])
    print("查看特征值：\n",iris.data,iris.data.shape)
    print("查看特征值的名字：\n",iris.feature_names)
    print(iris)#可以用dir()查看实例对象方法

    #数据集划分
    """
    训练集特征值 feature_train
    测试集特征值 feature_test
    训练集目标值 target_train
    测试集目标值 target_test
    """
    feature_train,feature_test,target_train,target_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
    print("训练集的特征值：\n",feature_train,feature_train.shape)  
    return None

def dict_demo():
    """
    字典特征抽取
    :return:
    """
    data = [{'city':'北京','temperature':100},{'city':'上海','temperature':60},{'city':'深圳','temperature':30}]
    # 1、实例化一个转化器类
    transfer = DictVectorizer(sparse=False) #Ture时 sparse矩阵（稀疏矩阵） 将非零值，按位置表示出来 节省内存（0都不表示）
    # 2、调用fit_transform()
    data_new = transfer.fit_transform(data)
    print(data_new)
    print(transfer.get_feature_names_out()) #是transfer不是data_new,data_new本质上还是transfer的一个方法产生的结果
    return None

def count_demo():
    """
    文本特征抽取
    :return:
    """
    data = ["life is short,i like like python","life is too long,i dislike python"]
    # 1、实例化一个转化器类
    transfer = CountVectorizer(stop_words=["is","too"]) # 不存在sparse参数，可以使用.toarray 方法
    print(transfer)
    # 2、调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new.toarray())
    print(transfer.get_feature_names_out())
    return None

def cut_word(text):
    """
    进行中文分词：“我爱北京天安门” --> “我 爱 北京 天安门”
    :paraam text:
    :return:
    """
    text= " ".join(list(jieba.cut(text))) #分词中间要有一个空格
    return text

def count_chinese_demo():
    """
    中文文本特征抽取，自动分词
    :return:
    """
    data = ["未来的你，遥不可及，无人可比","今天很残酷，明天更残酷，后天会很美好，但绝大多数人都死在明天晚上，却见不到后天的太阳"]
    data_new = []
    for i in data:
        data_new.append(cut_word(i))
    # 1、实例化一个转化器类
    transfer = CountVectorizer()
    # 2、调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print(data_final.toarray())
    print(transfer.get_feature_names_out())

    return None

if __name__ == "__main__":
    # 代码1：sklearn数据集使用
    # dataset_demo()
    # 代码2：字典特征抽取count
    # dict_demo()
    # 代码3：文本特征抽取
    # count_demo()
    # 代码4：中文文本特征抽取
    count_chinese_demo()

