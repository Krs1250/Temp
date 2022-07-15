import re

# t = int(input('input'))

def save(line,mode=1):
    if mode == 1:
        ulearning = open('ulearning\\选择.txt','a',encoding='utf-8')
    elif mode == 2:
        ulearning = open('ulearning\\填空.txt','a',encoding='utf-8')
    elif mode == 3:
        ulearning = open('ulearning\\判断.txt','a',encoding='utf-8')
    ulearning.write(line)
    ulearning.close


Q_1 = re.compile('<divclass="question-wrapperfinishedshow-answerright"data-bind="attr:{\'id\':\'question\'\+question.id\(\)},(.*?)</div></div><!--/ko--></div></div>')
Q = re.compile('<divclass="split-screen-wrapper"><!--koif:question.type\(\)==24--><!--/ko-->(.*?)</div><divclass="question-operation-wrapper"data-bind="">')
Q12 = re.compile(
    '<spandata-bind="attr:{\'class\':\'question-title-htmlquestion-type-\'\+question.type\(\)},html:question.title\(\)"class="question-title-htmlquestion-type-[1,2][multiple]*?">(.*?)</span></div>', re.S)
Q3 = re.compile(
    '<spandata-bind="attr:{\'class\':\'question-title-htmlquestion-type-\'\+question.type\(\)},html:question.title\(\)"class="question-title-htmlquestion-type-[3][multiple]*?">(.*?)</span></div>', re.S)
Q4 = re.compile(
    '<spandata-bind="attr:{\'class\':\'question-title-htmlquestion-type-\'\+question.type\(\)},html:question.title\(\)"class="question-title-htmlquestion-type-[4][multiple]*?">(.*?)</span></div>', re.S)

A1 = re.compile('<spanclass="input-wrapperright">(.*?</div>)</span>', re.S)
A2 = re.compile('<spanclass="answer-width">(.*?)</span>')
A12_option = re.compile('<divclass="option"data-bind="text:choice.option\(\)\+\'.\'">(.*?)</div>')
A12_text = re.compile('<divclass="text"data-bind="html:choice.title\(\)"role="button">(.*?)</div>')
A4 = re.compile('aria-label="已选中(.*?)"')
A12_real = re.compile('component.arrayToString\(question.correctAnswer\(\)\):question.correctAnswer\(\)\)">(.*?)</span>')

u = open('ulearning\\ulearning.txt', 'r', encoding="utf-8")
read = u.read()
read = read.replace(' ', "")
read = read.replace('\n', "")
read = read.replace('<br>','')
# print(read)
a1 = 'question-title-htmlquestion-type-1'
a2 = 'question-title-htmlquestion-type-2'
a3 = 'question-title-htmlquestion-type-3'
a4 = 'question-title-htmlquestion-type-4'

judge = re.findall(Q_1, read)

for i in judge:
    if a1 in i or a2 in i:
        '''
        选择题
        '''
        # pass
        answer = {}
        # print('a1')
        question = ''.join(re.findall(Q12, i))
        answer_option = re.findall(A12_option,i)
        answer_text = re.findall(A12_text,i)
        answer_real = ''.join(re.findall(A12_real,i))
        # print(question)
        # print(answer_option,answer_text)
        # print('----------------')
        for j in range(len(answer_option)):
            answer[j] = answer_option[j]+answer_text[j]
            # print(answer_option[j]+answer_text[j]+'\n')
        # print(question)
        # print(answer)
        # print(answer_real)
        save(question + '\n',mode=1)
        for j in range(len(answer)):
            save(answer[j]+'\n',mode=1)
        save('正确答案：'+ answer_real +'\n'+'\n',mode=1)
        
    elif a3 in i:
        '''
        填空题
        '''
        # pass
        result = re.findall(Q3,i)
        ans_t = re.findall(A2,''.join(result))
        # print(''.join(ans_t))
        answer = re.findall(A2,''.join(result))
        for j in ans_t:
            result = re.sub ('<spanclass="input-wrapperright"><inputtype="text"class="blank-input"disabled="disabled"><spanclass="answer-width">.*?/div></span>','('+j+')',''.join(result),1)
        result = ''.join(re.sub('&nbsp;','',''.join(result)))
        # print(result)
        # print('-----------------')
        save(result + '\n'+ '\n',mode=2)
    elif a4 in i:
        '''
        判断题
        '''
        # pass
        # print(i)
        question = ''.join(re.findall(Q4,i))
        answer = ''.join(re.findall(A4,i))
        # print(question)
        # print(answer)
        save(question + '\n' + '正确答案：' + answer + '\n' + '\n', mode=3)
    question = ''
    result = ''
    answer = ''
u.close()
print('done')