"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""

for num in range(1,10000):
    result = 0
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            result += i
    if result == num:
        print(num)