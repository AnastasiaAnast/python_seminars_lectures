# Задача 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# мн-во

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list_1 = set(list_1)
# count = len(list_1)
# print(count)
# ИЛИ
# n = [int(i) for i in input('Введите числа: ').split()]
# split - ф-я которая разделяет элементы строки
# n = set(n)
# print(len(n))

# Задача №19. 
# Дана последовательность СПИСОК[] из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# k = k % n

# data = [int(i) for i in input("Введите числа: ").split()]
# step = int(input("Введите кол-во сдвигов: "))
# step = step % len(data)
# data = [data[i - step] for i in range(len(data))]
# print(data)

#  0  1  2  3  4
# [1, 2, 3, 4, 5]
# -5  -4 -3 -2 -1
# k = 3
# [3, 4, 5, 1, 2]
#  2  3  4  0  1

# 0 - 3 = -3
# 1 - 3 = -2

# ИЛИ

# myList = [1, 2, 3, 6, 7, 8, -9, 0]
# n = int(input("Введите на какое кол-во элементов сдвинется список: ")) % len(myList)
# for i in range(n):
#     myList.insert(0, myList.pop())
# print(myList)

# отрицательная нумерация
# data = [int(i) for i in input("Введите числа: ").split()]
# for i in range((-1) * len(data), 0, +1):
#     print(data[i], i)

# [1, 2, 3]
# k = 1
# [3, 1, 2]

# k = 2
# [2, 3, 1]

# k = 3
# [1, 2, 3]

# k = 4
# [3, 1, 2]

# Задача №21. 
# Напишите программу для печати всех уникальных(!) значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# result = set()
# for item in data:
#     result.add(list(item.values())[0])
# print(result)
# ИЛИ
# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"},
#            {"VIII":"S007"}]
# result = set()
# for item in data:
#     for key in item:
#         result.add(item[key])
# print(*result)

# data = {'Ivan': 21, "Alexandr": 35, 'Mariy': 27}
# print(list(data.values()))
# print(list(data.keys()))

# data = {'Ivan': 21, "Alexandr": 35, 'Mariy': {'age': 27, 'hobby': 'tennis'}}
# print(list(data.values()))
# print(list(data.keys()))

# ИЛИ

# myList2 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# result2 = []
# for item in myList2 :
#     # result2.append(list(item)[0]) - выведет ключи, а не значения
#     result2.append(list(item.values())[0])
#     # result2.append(list(item.keys())[0])
# print(set(result2))

# Задача№23
# Дан массив, состоящий из целых чисел. Напишите программу, которая 
# подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# data = [int(i) for i in input("Введите числа: ").split()]
# count = 0
# for i in range(len(data) - 1):
#     if data[i + 1] > data[i]:
#         count += 1
# print(count)

# data = [int(i) for i in input("Введите числа: ").split()]
# data = [int(data[i + 1] > data[i]) for i in range(len(data) - 1)]
# print(data)
# print(sum(data))

# ИЛИ
# myList3 = [0, -1, 5, 2, 3]
# for i in range(1, len(myList3)):
#     if myList3[i] > myList3[i - 1]:
#         count += 1
# print(count)

# ИЛИ
# myList3 = [0, -1, 5, 2, 3]
# count = 0
# result = [myList3[i] for i in range(1, len(myList3))]
# print(result)