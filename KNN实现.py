#编程实现3NN

import numpy as np

#已有的数据集，第一列是分类标签
classlist = [[1, 2, 1],[1, 3, 1],[1, 2, 2],[2, 5, 2],[2, 5, 3],[2, 6, 3],[3, 2, 4],[3, 3, 4],[3, 3, 5]]
#print(classlist)

#设定k值
k = 5

#输入新的数据newdata
newdata = []
x1 = int(input("输入新数据坐标1: "))
x2 = int(input("输入新数据坐标2: "))
newdata.append(x1)
newdata.append(x2)


#生成距离列表dlist
dlist=[]
for i in range(9):
    d2 = (newdata[0]-classlist[i][1])*(newdata[0]-classlist[i][1])+(newdata[1]-classlist[i][2])*(newdata[1]-classlist[i][2])
    dlist.append(d2)
print("距离乱序版",dlist)

#排序列表
sorted_nums = sorted(enumerate(dlist), key=lambda x: x[1])
idx = [i[0] for i in sorted_nums]
nums = [i[1] for i in sorted_nums]
idxk=[]
for i in range(k):
    idxk.append(classlist[idx[i]][0])

print("距离排序版",nums)
print("距离对应的索引",idx)
print("前",k,"名距离对应的类别标签",idxk)

#输出众数
counts = np.bincount(idxk)
print("新数据归类：",np.argmax(counts))
print("————注意————")
print("算法是有bug的，对于相同的距离，排序上是很难进行区分的，分类可能因为某个类别的临近数据点冲突而被挤下排名，从而影响排序结果")
