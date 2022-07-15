
from urllib import response
from bs4 import BeautifulSoup # 网页解析，获取数据
import re # 正则表达式，进行文字匹配
import urllib.request,urllib.error # 指定URL，获取网页数据
import xlwt # 进行excel操作
import sqlite3 # 进行SQLite数据库操作

def main():
    #1、爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    askURL("https://ua.ulearning.cn/learnCourse/learnCourse.html?courseId=9866&chapterId=102778336&classId=509529&returnUrl=https%3A%2F%2Fcourseweb.ulearning.cn%2Fulearning%2Findex.html%23%2Fcourse%2Ftextbook%3FcourseId%3D100663")
    # datalist = getData(baseurl)
    #2、解析数据(逐一解析)
    savepath = ".\\豆瓣电影Top250.xls"
    #3、保存数据
    # saveData(savepath)

findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象（模板对象），表示规则（字符串的模式）
                                            # 加括号(.*?)就是捕获括号中的 不加括号就是全都匹配!?
#1、爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10): #调用获取页面信息的函数，10times
        url = baseurl + str(i*25)
        html = askURL(url)         #保存获取到的网页源码
    #2、解析数据(逐一解析)
    soup = BeautifulSoup(html,"html.parser")
    for  item in soup.find_all('div',class_="item"):   #查找符合要求的字符串，形成列表  #class是类别，要加下划线，否则会报错
        # print(item) #测试：查看电影item全部信息
        data = [] #保存一部电影的所有信息
        item = str(item)

        link = re.findall(findLink,item)[0] #re库用来通过正则表达式查找指定的字符串
        print(link)
    return datalist



#得到指定一个URL的网页内容
def askURL(url):
    head = {            #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
        }
                            #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件）
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8") #.decode方法防止字符串编码问题，重新转码
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):  #hasattr 获取标签，用于捕获
            print(e.code) #e.code不存在
        if hasattr(e,"reason"):
            print(e.reason)

    return html # 


    #3、保存数据
def saveData(savepath):
    pass


    







if __name__ == "__main__":
    main()