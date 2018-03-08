# _*_ coding:UTF-8 _*_

# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。
# 程序源代码：

a = [1, 2, 3]
b = a[:]
c = a*1
c.append(8)
b.append(4)
print "a:",a
print "b:",b
print "c:",c

# 补充一个深拷贝与浅拷贝的问题
import copy
#浅拷贝 ,拷贝链接
d = ['X', 'Y', a]
print "d:", d
a[0] = 11
print "a:", a
print "d:", d

#深拷贝 ,拷贝值
e = copy.deepcopy(d)
a[0] = 111
print "a:", a
print "e:", e
