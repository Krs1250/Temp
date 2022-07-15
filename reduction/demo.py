import re

find_1 = re.compile('href="(.*?)"')

file_path =  r'reduction\a1.txt'


with open(file_path,'r',encoding='utf-8') as file:
    text = file.read()
    text = text.replace('<thead>','')
    text = text.replace('<tbody>','')
    text = text.replace('</thead','')
    text = text.replace('</tbody>','')
    text = text.replace(' style="vertical-align: top;',' ')
    text = text.replace(' scope="col"',' ')
    text = text.replace('strong','b')
    text = text.replace('code','pre')
    text = text.replace('</b>','</b> ')
    text = re.sub(find_1,'href="#"',text)
    text = re.sub('td "','td',text)
    text = re.sub('<td><a href="#"><pre>','<td><a href="#">',text)
    text = re.sub('</pre></a></td>','</a></td>',text)
    print(text)
