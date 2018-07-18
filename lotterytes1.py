#-*-coding:utf-8 -*-

#根据提供的名单进行抽奖

import random

#名单
plist = []

print('--开始输入抽奖人,输入完毕输入quit结束--')
i = 1
person = ''
while True:
    person = input('正在输入第{}个：'.format(i))
    if person == 'quit':
        if len(plist) < 6:
            print('输入的名单人数不够，请继续输入！')
            continue;
        else:
            print('输入名单结束！')
            break;
    plist.append(person)
    i = i + 1

#抽取三个三等奖
pthree = []
p3 = ''
for j in range(1,4):
    p3 = random.choice(plist)
    pthree.append(p3)
    plist.remove(p3)

print('3个三等奖是：'+str(pthree))

#抽取两个二等奖
ptwo = []
p2 = ''
for j in range(1,3):
    p2 = random.choice(plist)
    ptwo.append(p2)
    plist.remove(p2)

print('2个二等奖是：'+str(ptwo))

#抽取一等奖
p1 = random.choice(plist)

plist.remove(p1)

print('一等奖是：'+p1)