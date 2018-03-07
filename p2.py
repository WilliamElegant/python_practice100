# _*_ coding:UTF-8 _*_

# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

# 第一种方法：使用 if...elseif...来完成

bonus = 0L
profit = int(raw_input('pure profit:'))
if profit <= 10:
    bonus = profit * 0.1
elif profit <= 20:
    bonus = 10 * 0.1 + (profit - 10) * 0.075
elif profit <= 40:
    bonus = 10 * 0.1 + 10 * 0.075 + (profit - 20) * 0.05
elif profit <= 60:
    10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (profit - 40) * 0.03
elif profit <= 100:
    10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (profit -60) * 0.015
else:
    10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (profit -100) * 0.01

print bonus

# another way
# 使用字典控制利润与提成比例的匹配

num = int(raw_input("输入利润："))

obj = {100: 0.01, 60: 0.015, 40: 0.03, 20: 0.05, 10: 0.075, 0: 0.1}
keys = obj.keys()
keys.sort()
keys.reverse()
bonus1 = 0L

for key in keys:
    if num > key:
        bonus1 += (num - key) * obj.get(key)
        num = key  # here is the point
print "bonus is:", bonus1