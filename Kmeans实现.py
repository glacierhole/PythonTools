#Kmeans实现
#设定数据集
N=9
classlist = [[10, 2, 1],[1, 3, 1],[1, 2, 2],[2, 5, 2],[2, 5, 3],[2, 6, 3],[3, 2, 4],[3, 3, 4],[3, 3, 5]]


#设定分类值k
k = 3
#预设k个聚类中心
C1 = [1,1,1]
C2 = [2,3,2]
C3 = [5,5,5]
#大循环M次，停止迭代
M=13
for j in range(M):
    #根据距离归类
    class1 = []
    class2 = []
    class3 = []
    for i in range(N):
        dd1 = (C1[0]-classlist[i][0])*(C1[0]-classlist[i][0])+(C1[1]-classlist[i][1])*(C1[1]-classlist[i][1])+(C1[2]-classlist[i][2])*(C1[2]-classlist[i][2])
        dd2 = (C2[0]-classlist[i][0])*(C2[0]-classlist[i][0])+(C2[1]-classlist[i][1])*(C2[1]-classlist[i][1])+(C2[2]-classlist[i][2])*(C2[2]-classlist[i][2])
        dd3 = (C3[0]-classlist[i][0])*(C3[0]-classlist[i][0])+(C3[1]-classlist[i][1])*(C3[1]-classlist[i][1])+(C3[2]-classlist[i][2])*(C3[2]-classlist[i][2])
        if (dd1<=dd2)&(dd1<dd3):
            class1.append(classlist[i])
        elif (dd2<dd1)&(dd2<=dd3):
            class2.append(classlist[i])
        elif (dd3<=dd1)&(dd3<dd2):
            class3.append(classlist[i])
    print("第",j+1,"次循环")
    print("类别1的元素个数",len(class1),"元素为",class1)   
    print("类别2的元素个数",len(class2),"元素为",class2)
    print("类别3的元素个数",len(class3),"元素为",class3)
    #计算新的聚类中心
    C1=[0,0,0]
    C2=[0,0,0]
    C3=[0,0,0]
    for x in range(len(class1)):
        C1[0] += class1[x][0]
        C1[1] += class1[x][1]
        C1[2] += class1[x][2]
    for y in range(len(class2)):
        C2[0] += class2[y][0]
        C2[1] += class2[y][1]
        C2[2] += class2[y][2]
    for z in range(len(class3)):
        C3[0] += class3[z][0]
        C3[1] += class3[z][1]
        C3[2] += class3[z][2]
    C1[0]=C1[0]/len(class1)
    C1[1]=C1[1]/len(class1)
    C1[2]=C1[2]/len(class1)
    C2[0]=C2[0]/len(class2)
    C2[1]=C2[1]/len(class2)
    C2[2]=C2[2]/len(class2)
    C3[0]=C3[0]/len(class3)
    C3[1]=C3[1]/len(class3)
    C3[2]=C3[2]/len(class3)



