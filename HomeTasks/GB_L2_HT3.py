# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

n = int(input('input N: '))
list = [1]

number = 2
while number < n:
    list.append(number)
    number *= 2

print(list)
