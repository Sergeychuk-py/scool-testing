import random

squares = []
for i in range(1, 9 + 1):
    squares.append(i * 2)
print(squares)

r = [i * 3 for i in range(1, 8)]
print(r)


def get_heith_prise(percent, price):
    return round(price * (1 + percent / 100), 2)


prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_yaer = random.randint(1, 11)
second_yaer = random.randint(1, 21)
result_1 = [get_heith_prise(first_yaer, _price) for _price in prices_now]
result_2 = [get_heith_prise(second_yaer, _price_2) for _price_2 in prices_now]
print(f'Сумма за каждый год: {sum(result_1)}\n{sum(result_2)}')

squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]
print(squares_odds)

squares_cubes = [x ** 2 if x % 2 != 0 else x ** 3 for x in range(10)]
print(squares_cubes)

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_condition = [('Погиб' if squad_1[i_damage] + squad_2[i_damage] > 100
                    else 'Выжил'
                    )
                   for i_damage in range(10)]
print(f'\nУрон первого отряда: {squad_1}')
print(f'Урон второго отряда: {squad_2}')
print(f'Состояние третьего отряда: {squad_condition}\n')

first_num = 1
second_num = 11

even_numbers = [x for x in range(first_num, second_num + 1) if x % 2 == 0]
print(even_numbers, '\n')

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# Проходим по каждому элементу списка
for i in range(len(original_prices)):
    # Если элемент отрицательный, заменяем его на 0
    if original_prices[i] < 0:
        original_prices[i] = 0

# Выводим список чисел после замены отрицательных чисел на 0
print(original_prices)

n_prices = [0 if i < 0 else i for i in original_prices]
print(n_prices)

"""Срезы """

nums = [x for x in range(1, 100 + 1) if x % 10 == 0]
n_nums = nums[:]
n_nums[3] = 0

for i_elem in range(2, 8):
    print(n_nums[i_elem], end=' ')

# СРЕЗЫ
# nums = [x for x in range(1, 100 + 1) if x % 10 == 0]
# nums[2:7]  диапозон индексов, с 2 по 7
# [30, 40, 50, 60, 70]
# nums[:7] стврт с нулевого индекса по 7
# [10, 20, 30, 40, 50, 60, 70]
# nums[7:] старт с 7 индекса
# [80, 90, 100]
# nums[2:8:2] диапозон индексов с 2 по 8 с шагом 2
# [30, 50, 70]
# nums[-1] последние число в списке
# 100
# nums[::-1] разворачиваем список
# [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]


# arr = [1, 2, 2, 3, 3, 3]
# print('\n\n', set(arr))


# dick = [_ for _ in range(1, random.randint(1, 1000))]
#
# print(dick)


nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
new_nums = nums[:]

print('\n', new_nums[0:5])
print('\n', new_nums[0:7])
print('\n', new_nums[::2])
print('\n', new_nums[::3])
print('\n', new_nums[::-1])
print('\n', new_nums[-1])


def stringies(word: str):
    l = len(word) + 1
    part_1 = word[0:l // 2]
    part_2 = word[l // 2:]
    return part_1[::-1] + part_2[::-1]


print(stringies('Привет'), '\n')


class User:
    name = 'Serg'
    password = '0000'
    is_banned = False

user = User()
user.name = 'Tom'
print(user.name)
print(user.password)
print(user.is_banned)
