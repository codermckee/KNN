# -*- coding: utf-8 -*-
import random

def generate_data(min1,max1,min2,max2,min3,max3,len):
    info = []
    for i in range(len):
        buf = []
        height = random.uniform(min1, max1)
        weight = random.uniform(min2, max2)#可能体重作为属性不太好，因为不同身高段的人体重可能在同一个小范围内。仅作为试验
        leg_length = random.uniform(min3, max3)
        buf.append(height)
        buf.append(weight)
        buf.append(leg_length)
        info.append(buf)
    return info
def save(info,label):
    handle = open('data.txt','a+')
    for i in info:
        print i[0],i[1],i[2]
        handle.write(str(i[0])+' ')
        handle.write(str(i[1])+' ')
        handle.write(str(i[2])+' ')
        handle.write(label)
        handle.write('\n')
    handle.close()

if __name__ == '__main__':
    model = generate_data(169.9,180,90,110,105,111,50)
    lolita = generate_data(155,162,85,98,95,100,50)
    common = generate_data(162,169,80,115,100,104.5,50)
    save(model,'model')
    save(lolita,'lolita')
    save(common,'common')


