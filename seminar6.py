# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# from random import randint as rd


# n = int(input())
# list_1 = [rd(1, 11) for i in range(n)]
# print(list_1)
# m = int(input())
# list_2 = [rd(1, 11) for j in range(m)]
# print(list_2)
# for i in list_1:
#     if i not in list_2:
#         print(i, end=' ')

#  ИЛИ

# from random import randint as rd


# n = int(input())
# list_1 = [rd(1, 11) for i in range(n)]
# print(f'---------------------\nСписок 1: {list_1}\n------------------')
# m = int(input())
# list_2 = [rd(1, 11) for j in range(m)]
# print(f'---------------------\nСписок 2: {list_2}\n------------------')
# print('Результат:', [i for i in list_1 if i not in list_2])


# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# n = int(input())
# list_1 = [int(i) for i in input().split()][:n]
# print(sum([int(list_1[i - 1] < list_1[i] > list_1[i + 1]) for i in range(1, n - 1)]))


# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

# решение через словарь

# list_1 = [int(i) for i in input().split()]
# result = {}
# for element in list_1:
#     if element in result:
#         result[element] += 1
#     else:
#         result[element] = 1
# print(sum([i // 2 for i in result.values()]))

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

# n = int(input())
# list_1 = list()
# for i in range(n):
#     summa = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#             summa += j
#     list_1.append((i, summa))
# print(list_1)
# for i in range(len(list_1)):
#     for j in range(i, len(list_1)):
#         if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
#             print(*list_1[i])