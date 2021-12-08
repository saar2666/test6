list = ['1','2','3','a','a','b','c','2','c','1']


def removeDups(list):
    y = []
    for i in list:
        if i not in y:
            y.append(i)
    return y

print(removeDups(list))
