# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random

n = int(input('Input coins quantity: '))

coins = [random.randint(0,1) for i in range(n)]
result = sum(coins)
if result > n - result:
    result = n - result

print(coins)
print(result)