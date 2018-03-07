#!
# _*_ coding: UTF-8 _*_

'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
程序源代码：
'''
amount = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != j) and (j != k):
                print i, j, k
                amount += 1
print 'total:', amount

print 'another way:'
# 直接用列表推导式
a = [(x, y, z) for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) if(x != y) and (x != z) and (y != z)]
print a