# -*- coding: utf-8 -*-
import random
import math
def get_train_data():
    test = []
    train = []
    handle = open('data.txt')
    for line in handle:
        line = line.strip().split()
        if random.random() < 0.333333333333:
            test.append(line)
        else:
            train.append(line)
    return train,test
def cal_distance(a,b,dimension):#用的是欧几里得距离
    d = 0
    for i in range(dimension):
        d += (float(a[i])-float(b[i]))*(float(a[i])-float(b[i]))
    d = math.sqrt(d)
    return d
def get_neighbor(K,test,train_data):
    distance = []
    neighbor = []
    for i in range(len(train_data)):
        info = []
        l = cal_distance(test,train_data[i],3)
        label = train_data[i][-1]
        info.append(l)
        info.append(label)
        distance.append(info)
    distance = sorted(distance)
    for i in range(K):
        neighbor.append(distance[i])
    return neighbor

def get_prediction(K,neighbor):
    model_num = 0
    common_num = 0
    lolita_num = 0
    for i in range(K):
        if neighbor[i][1] == 'model':
            model_num += 1
        elif neighbor[i][1] == 'common':
            common_num += 1
        else:
            lolita_num += 1
    if model_num > common_num and model_num > lolita_num:
        prediction = 'model'
    elif lolita_num > model_num and lolita_num > common_num:
        prediction = 'lolita'
    else:
        prediction = 'common'
    return prediction
def evaluate_Accuracy(test,train,K):
    neighbor_set = []
    prediction_set = []
    for i in range(len(test)):
        neighbor_buf = get_neighbor(K,test[i],train)
        prediction = get_prediction(K,neighbor_buf)
        prediction_set.append(prediction)
        neighbor_set.append(neighbor_buf)
    #print neighbor_set[0]
    #print prediction_set
    right = 0
    for i in range(len(prediction_set)):
        if prediction_set[i] == test[i][-1]:
            right += 1
    precision = float(right)/float(len(prediction_set))
    return precision

if __name__ == '__main__':
    K = 5
    train_data, test_data = get_train_data() #得到训练集与测试集
    #print train_data
    #print test_data
    precision = evaluate_Accuracy(test_data, train_data, K) #评定精度
    print precision

    test = [172, 96, 106]
    neighbor = get_neighbor(K,test,train_data) #得到最近邻的K个值
    prediction = get_prediction(K,neighbor) #对样本作预测
    print 'Girl Type:', prediction

