a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

commonList = []
for i in a:
    if i in b and i not in commonList:
        commonList.append(i)

print(commonList)



#result = [i for i in a if i in b] //shorter verion for the for