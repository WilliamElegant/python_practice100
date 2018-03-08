# _*_ coding:UTF-8 _*_

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
# 程序源代码：

# l = []
# for i in range(3):
#     x = int(raw_input("input a number:"))
#     l.append(x)
#
# l.sort()
# print l

elements = (4, 3, 5, 2, 6, 1, 7)

ele1 = sorted(elements)
ele2 = list(reversed(sorted(elements)))

print ele1
print ele2

# 学习 python sorted() 函数，同时附带讲解 sorted() 和 sort() 方法的区别。详见有道云笔记

a = [5,7,6,3,4, 1, 2,0]
b = sorted(a)
print "a:", a
print "b:", b

students = [('John', 'A', 15),('Mary', 'C', 12),('Tom', 'B', 20)]
# sorted by age
s = sorted(students, key = lambda s: s[2])
print "sort by age:", s
# sorted by level
s1 = sorted(students, cmp = lambda x,y: cmp(x[1],y[1]))
print "sort by level:", s1




