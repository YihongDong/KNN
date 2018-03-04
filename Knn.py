from numpy import *
from pylab import *
from sklearn.decomposition import PCA
from readdata import *
from feature_change import *
from sklearn.model_selection import LeavePOut


def KNN(test, data, label, k):
    # data, mean, max = feature_change(data)
    data = mat(data)
    mytest = mat(test)
    label_result = []
    for i in range(len(mytest)):
        dist = data - mytest[i]
        distance = []
        for j in range(len(data)):
            distance.append((float(dist[j] * dist[j].T), j))
        distance_sorted = sorted(distance)
        true = 0
        false = 0
        for l in range(k):
            if label[distance_sorted[l][1]] == 1:
                true = true + 1
            else:
                false = false + 1
        if true > false:
            label_result.append(1)
        else:
            label_result.append(0)
    return label_result


def KNN1(test, data, label, k):
    mytest = mat(test)
    label_result = []
    for i in range(len(mytest)):
        distance = []
        dist = data - mytest[i]
        for j in range(len(data)):
            distance.append([float(dist[j] * dist[j].T), j])
        distance_sorted = sorted(distance)
        true = 0
        false = 0
        # print(distance_sorted)
        for l in range(k):
            if label[distance_sorted[l][1]] == 1:
                true = true + 1
            else:
                false = false + 1
        if true > false:
            label_result.append(1)
        else:
            label_result.append(0)
    return label_result

def KNN_decision(data, label, k):
    data = mat(data)
    for i in arange(150,190,1):
        for j in arange(40,90,1):
            distance = []
            dist = data - array([i,j])
            for k in range(len(data)):
                distance.append([float(dist[k] * dist[k].T), k])
            distance_sorted = sorted(distance)
            if label[distance_sorted[1][1]]==1:
                plot(i,j,'.',color='g')
            else :
                plot(i,j,'.',color='k')




def main():
    # train
    x = []
    label = []
    path_boy = "F:\\study in school\\machine learning\\forstudent\\实验数据\\boynew.txt"
    path_girl = "F:\\study in school\\machine learning\\forstudent\\实验数据\\girlnew.txt"
    readdata(path_boy, x, label, 1)
    readdata(path_girl, x, label, 0)
    # data, mean, max = feature_change(x)
    # test
    x_test = []
    label_test = []
    path_boy_test = "F:\\study in school\\machine learning\\forstudent\\实验数据\\boy.txt"
    path_girl_test = "F:\\study in school\\machine learning\\forstudent\\实验数据\\girl.txt"
    readdata(path_boy_test, x_test, label_test, 1)
    readdata(path_girl_test, x_test, label_test, 0)
    pca = PCA(n_components=3)
    pca.fit(x)
    print(pca.components_)
    x=mat(x)*pca.components_.T
    figure(1)
    for i in range(len(x)):
        if label[i] == 1:
            plot(x[i,0], x[i,1], 'o', color='r')
        else:
            plot(x[i,0], x[i,1], 'x', color='b')
    show()

    # 剪辑
    # loo = LeavePOut(p=35)
    # error = 0
    # s=[]
    # for train, test in loo.split(x, label):
    #     mytest = KNN(x[test],x[train],label[train],1)
    #     for i in range(len(mytest)):
    #         if mytest[i]!=label[train[i]]:
    #             s.append([x[train[i]],label[train[i]]])
    # print(s)

    # # KNN
    # label_result = KNN(x_test, x, label, 1)
    # error = 0
    # for i in range(len(label_test)):
    #     if label_result[i] != label_test[i]:
    #         error = error + 1
    # error_percentage = error / len(label_test)
    # print(error_percentage)
    # X=[]
    # Y=[]
    # for k in arange(1,21,2):
    #     label_result = KNN(x_test, x, label, k)
    #     error = 0
    #     for i in range(len(label_test)):
    #         if label_result[i] != label_test[i]:
    #             error = error + 1
    #     error_percentage = error / len(label_test)
    #     X.append(k)
    #     Y.append(error_percentage)
    # figure(2)
    # plot(X,Y)
    # show()



main()
