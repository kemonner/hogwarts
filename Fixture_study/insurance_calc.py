"""
    保险收益计算：
        1.基本保险金Y：19225，33-60岁之间，年反Y*0.15=2883
        2.如果不取出，年化利息3%累积
        计算27年后，年金加利息和。
"""

a = 2969.49   # 2027年发放第一笔，2028年第一次结算本金加利息2969.49。
insurance_m = [2969.49]
for i in range(27):
    a = (a+2883)*0.03+(a+2883)
    insurance_m.append(round(int(a)))
print(insurance_m)
print('累积27年后年金加利息和为：', max(insurance_m))
