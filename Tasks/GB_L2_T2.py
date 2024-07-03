# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

a = 22
i = 4
fibNum = 2
fibPrevNum = 1
flag = True

while flag:
    if a == fibNum:
        flag = False
    elif a < fibNum:
        i = -1
        flag = False
    else:
        i += 1
        temp = fibNum
        fibNum += fibPrevNum
        fibPrevNum = temp

print(i)