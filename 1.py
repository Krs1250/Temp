text = str(input("输入文本："))
text=text.replace('<',r'<pre>&lt;')
text=text.replace('>',r'&gt</pre>;')
text=text.replace('HTML','<b>HTML')
text=text.replace('元素','元素</b>')

print(text)
