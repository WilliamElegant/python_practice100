# _*_ coding:UTF-8 _*_

# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：
# 程序源代码：

year = int(raw_input("input the year:"))
month = int(raw_input("input the month:"))
day = int(raw_input("input the day:"))

days_in_pre_month = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
total = 0

if 0 < month <= 12:
    total = days_in_pre_month[month - 1]
else:
    print 'input month error'

total += day
leap = 0

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1

if (leap == 1) and (month > 2):
    total += 1

print '输入的是该年的第 %d 天' % total

# another way
# use lib
# familiar with time package and strptime function and its response object
import time
inputDate = raw_input("请输入日期，格式yyyyMMdd:")
day = time.strptime(inputDate, '%Y%m%d').tm_yday
print "输入的日期是今年的第 %d 天" % day

