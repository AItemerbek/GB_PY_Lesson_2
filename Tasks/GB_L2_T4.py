# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

import random
minWeight = 10
maxWeight = 0

n = int(input('Input watermellon quantity: '))
for i in range(n):
    weight = random.randint(1,10)
    print(weight, end= ' ')
    if weight <= minWeight:
        minWeight = weight
    if weight >= maxWeight:
        maxWeight = weight
print(end='\n')
print(f'Max = {maxWeight}, Min = {minWeight}')
