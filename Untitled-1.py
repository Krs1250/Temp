ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
head = 0
print(ListValue[head])
next = ListRight[head]
while next != -1:
    print(ListValue[next])
    next = ListRight[next]