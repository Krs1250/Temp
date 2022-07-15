from cgi import print_arguments
from ctypes.util import find_library
from gettext import find
import re
from tkinter import Tk


T = []
Q = []
A = []
RA = []

Qp = re.compile('<spandata-bind="attr:{\'class\':\'question-title-htmlquestion-type-\'\+question.type\(\)},html:question.title\(\)"class="question-title-htmlquestion-type-[1,2][multiple]*?">(.*?)</span>',re.S)
QBp = re.compile('<spandata-bind="attr:{\'class\':\'question-title-htmlquestion-type-\'\+question.type\(\)},html:question.title\(\)"class="question-title-htmlquestion-type-[1,2,4][multiple]*?">(.*?)\&nbsp;',re.S)
Ap = re.compile('<div class="text" data-bind="html: choice.title\(\)" role="button">(.*?)</div>',re.S)
RAp = re.compile('<spandata-bind="html:question.type\(\)==4\?\(question.correctAnswer\(\)==true\?\$root.i18nMessageText\(\).right:\$root.i18nMessageText\(\).wrong\):\(question.type\(\)==3\?\$component.arrayToString\(question.correctAnswer\(\)\):question.correctAnswer\(\)\)">(.*?)</span>')
RABp = re.compile('<spandata-bind="html:question.type\(\)==4\?\(question.correctAnswer\(\)==true\?\$root.i18nMessageText\(\).right:\$root.i18nMessageText\(\).wrong\):\(question.type\(\)==3\?\$component.arrayToString\(question.correctAnswer\(\)\):question.correctAnswer\(\)\)">(.*?)&nbsp;')


def getInf(p=1): 
    '''
    p == 1 为选择
    p == 2 为判断
    p == 3 为填空
    '''
    u = open('ulearning\\ulearning.txt','r',encoding="utf-8")
    read = u.read()
    read = read.replace('\n','')
    read = read.replace(' ','')
    if p == 1 or p == 2:
        findQ = re.findall(Qp, read)
        findA = re.findall(Ap, read)
        findRA = re.findall(RAp,read)
        for i in range(len(findQ)):
            Q.append(findQ[i])
            A.append(findA[4*i:4*i+4])#改
            RA.append(findRA[i])
        if p == 1:
            solveInf_choice()
        elif p ==2:
            solveInf_judge()
    elif p == 3:
        pass
    u.close()
    print(re.search(Qp,read))
    u.close()
def solveInf_choice():
    '''
    选择题
    '''
    u = open('.\\ulearning\\题库1.txt','a',encoding="utf-8")
    for i in range(len(Q)):
        u.write('%d.'%(i+1) + Q[i]+'\n')
        u.write('  .'+str(A[i][0])+'\n')
        u.write('  .'+str(A[i][1])+'\n')
        u.write('  .'+str(A[i][2])+'\n')
        try:
            u.write('  .'+str(A[i][3])+'\n')
        except IndexError:
            print('123')
        u.write('正确答案：'+RA[i]+'\n')
        u.write('\n')
    u.close()

def solveInf_blank():
    '''
    填空题
    '''
    u= open('.\\ulearning\\题库1.txt','a',encoding="utf-8")
    for i in range(len(Q)):
        u.write('%d.'%(i+1) + Q[i]+' _'+RA[i]+'_ '+'\n')
    u.close

def solveInf_judge():
    '''
    判断题
    '''
    u = open('.\\ulearning\\题库1.txt','a',encoding="utf-8")
    for i in range(len(Q)):
        u.write('%d.'%(i+1) + Q[i]+'\n')
        u.write('正确答案：'+RA[i]+'\n')
        u.write('\n')
    u.close


if __name__ == "__main__":
    getInf(3)
    # solveInf_choice()
    # solveInf_judge()
    # solveInf_blank()