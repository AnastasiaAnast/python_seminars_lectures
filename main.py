'''
ЛЕКЦИЯ 1      ЛЕКЦИЯ 1        ЛЕКЦИЯ 1        ЛЕКЦИЯ 1        ЛЕКЦИЯ 1

Python - язык с ДИНАМИЧЕСКОЙ ТИПИЗАЦИЕЙ данных - сам определяет какой тип данных присвоить переменной, в отличии от java и C++, которые явл статистически типизированными языками и где требуется явно указывать тип переменных. Отсюда главный минус Python - скорость, по факту мы пишем скрипт(код), а делее этот скрипт передается интерпретатору, интерпретатор тратит много времени на определение данных. Если на компьютере нет интерпретатора python - скрипт превращается в обычный текстовый файл.
После создания папки в вс код и файла(.py) для работы требуется настроить виртуальное окружение (чтобы работать с разными версиями библиотек) - в терминале вводим: python3 -m venv .folder   - создастся необходимая папка .folder
'''
# number1 = 10
# print(number1) # вывести переменную number1
# print("это строка") # вывести строку "это строка" (строки можно писать с одной ' и двумя " кавычками)
# print(1, 2, 3) # вывести 1, 2, 3

# n = 5 #тип данных int
# n = 1.89  #тип данных float/ вещественный тип данных

# n = None #тоже тип данных; присвоить пустое значение переменной - потребуется позже, но еще не ясно, какой тип данных будет иметь
# print(type(n)) # <NoneType> вывести тип данных переменной n с помощью ф-и type

# чтобы вывести внутри строки одну кавычку(одинарную или двойную) нужно использовать /' или /"
# чтобы внутри строки сделать ПЕРЕХОД на НОВУЮ СТРОКУ исп \n внутри строки
# n = "это текст 'привет'" #чтобы использовать две кавычки внутри строки - достаточно чтобы они отличались от кавычек, обрамляющих строку - если обрамляют "" - исп ' и наоборот '' - ".

# Интерполяция - получение сложной строки из нескольких простых с помощью шаблонов
# f-строки:
# print(f"") - print(f"{a} - {b} - {c}") # внутри фигурных скобок пишем имена переменных, между - символы, которыми хотим разделять переменные.
# print("{} - {} - {}".format(a,b,c))
# print("{1} - {2} - {0}".format(a,b,c)) # внутри фиг скобок пишем индексы (также с 0) - так можно менять последовательность вывода переменных

# вместо массивов (как в C#) в python - списки - list_1 = []
# в списке можно миксовать различные типы данных, но лучше хранить данные одного типа

# Ввод данных - ф-я input
# input() #значение НЕ сохранится после ввода
# n = input() #чтобы значение сохранилось - запишем значение в переменную n

# c = input("Введите второе число: ") # ф-я input() ВВОДИТ СТРОКУ!!!
# a = int(input()) # ПРЕОБРАЗОВАНИЕ в int
# b = input("Введите второе число: ")

# произведем операцию сложения внутри ф-ии print
# print(a, " + ", b, " = ", a + b) # ф-я print() тоже ВВОДИТ СТРОКУ!!! здесь ответ будет прим: 3+4=34
# при умножении строки на число - строка повторится столько раз, на сколько была умножена

'''
Приведение типов (int, str, float, bool)
c = int(b)
c = str(b)
c = bool(b)
'''
# c = 5.89
# print(c)
# print(type(c)) #type float
# c = int(c)
# print(c) #отбросит все, что после запятой, БЕЗ ОКРУГЛЕНИЯ
# print(type(c))  #type int

# символы кирилицы и латиницы нельзя перевести в int, float

''' 1 и 0 можно привести в БУЛЕВЫЙ тип -        1 = TRUE,      0 = FALSE '''


'''
Арифметические операции: 

+ сложение          - вычитание         * умножение         / деление (по умолчанию только в вещественных числах)
% остаток от деления        // целочисленный остаток от деления     ** возведение в степень

'''
# a = 5.968349
# b = 6.723985
# print(round(a*b, 3))
# #ф-я округления чисел round, принимает на вход 2 аргумента - 1-е число, 2-е ЧИСЛО ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ

# iter = 2 # iter - итерация
# iter += 3 # новой переменной iter присваивается значение старой переменной iter + 3
# iter -= 4
# iter *= 5
# iter /= 5
# iter //= 5 # новой переменной iter присваивается ЦЕЛОЧИСЛЕННОЕ значение от деления старой переменной iter на 5
# iter %= 5 # новой переменной iter присваивается ОСТАТОК от деления старой переменной iter на 5
# iter **= 5 # новой переменной iter присваивается значение старой переменной iter, возведенное в 5-ю СТЕПЕНЬ

'''
Логические операции: 
>       >=      <       <=      ==      !=      not - ОТРИЦАНИЕ     and - КОНЪЮНКЦИЯ     or - ДИЗЪЮНКЦИЯ
'''
# a = 1 > 4
# print(a) # false

# a = 1 < 4 and 5 > 2
# print(a) # true

# a = 1 == 2
# print(a) # false

# a = 1 != 2
# print(a) # true

# a = "qwe"
# b = "qwe"
# print(a == b) # true 

# a = 1 < 3 < 5 < 10 # можно сравнить сразу несколько чисел между собой и выражение будет записано в переменную
# print(a) # true

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f) # true - проверяем: "содержится  2 в списке f?"
# print(not 2 in f) # false - проверяем: "НЕ содержится 2 в списке f?"
# is_odd = f[0] % 2 == 0 # false; проверить факт ЧЕТНОСТИ ЧИСЛА из списка
# print(is_odd)
'''
АЛГЕБРА ЛОГИКИ - 6 логических операций: >, >=, <, <=, ==, !=
(+ is, is not, in, not in)
Логическая переменная принимает логические знач-я: true — false, 1 — 0.
Лог переменная полностью описана табл истинности, указывающей, какие значение принимает составное высказывание.
— отрицание (инверсия, логическое НЕ)
А       не А
0       1
1       0

— конъюнкция (логическое умножение, логическое И)
Высказывание истинно, когда истинны оба исходных высказывания.
А       В       А и В
0       0       0
0       1       0
1       0       0
1       1       1

— дизъюнкция (логическое сложение, логическое ИЛИ)
Высказывание ложно, когда ложны оба исходных высказывания.
А       В       А или В
0       0       0
0       1       1
1       0       1
1       1       1

- импликация (→) - логическое следование, "если ..., то" - новое высказывание, кот явл ложным, когда ПЕРВОЕ высказывание (посылка) ИСТИННО, а ВТОРОЕ (следствие) — ЛОЖНО. Во всех ост случаях - высказывание истинно.
А       В       А → В
0       0       1
0       1       1
1       0       0
1       1       1

- дизъюнкция (⊕) строгая, исключающая - логич операция, (ЛИБО, выполнение обоих условий одновременно невозможно) ставящая в соответствие двум высказываниям новое, явл истинным, когда только одно из двух высказываний истинно.
А       В       А ⊕ В
0       0       0
0       1       1
1       0       1
1       1       0

- эквиваленция/равнозначность (↔) "тогда и только тогда, когда" - логич операция, ставящая в соответствие двум высказываниям новое, являющееся истинным, когда оба исходных высказывания истинны или оба исходных высказывания ложны.
А       В       А ↔ В
0       0       1
0       1       0
1       0       0
1       1       1

'''




'''
управляющие конструкции if и if-else (если: делается одно действие - иначе: делается другое действие)
'''
# if условие/condition:
#     оператор 1
#     оператор 2
#      ...
#     оператор n
# else:
#     оператор n + 1
#     оператор n + 2
#     оператор n + m

''' elif == else if         проверяем первое условие, если оно не выполняется - второе и так далее. Как только будет найдено верное условие, остальные будут игнорироваться'''

# if condition1:
#     operator
# elif condition2:
#     operator
# elif condition3:
#     operator
# else:
#     operator

''' сложные условия - создаются с помощью логических операторов and, or, not '''

# if condition1 and condition2: #выполняется когда ОБА условия истинны
#     operator
# if condition3 or condition4: #выполняется когда ОДНО из условий истинно
#     operator
# if condition3 not condition4: #выполняется когда условия НЕ равны друг другу
#     operator

# username = input("Введите имя: ")
# if username == "Маша":
#     print("О нет, это снова Маша")
# elif username == "Марина":
#     print("Приветствую, Марина!")
# elif username == "Ильнар":
#     print("Приветствую, Ильнар!")
# else:
#     print("Привет, ", username)

# username = input("Введите имя: ")
# if username != "Маша":
#     print("Слава богу, это не  Маша")

''' Цикл while - выполняется до тех пор, пока верно условие, написанное возле него '''

# while condition:
#     operator 1
#     operator 2
#     ...
#     operator n

# n = 423
# sum = 0
# while n > 0:
#     x = n % 10
#     sum = sum + x
#     n = n // 10
# print(sum)

''' Управляющая конструкция while-else - выполняется только в случае, если осн тело цикло завершило работу самостоятельно (без оператора break) '''

# while condition:
#     operator 1
#     operator 2
#     ...
#     operator n
# else: # выполняется только в случае, если осн тело цикло завершило работу без оператора break
#     operator n + 1
#     operator n + 2
#     ...
#     operator n + m

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i += i
# else: # здесь блок else выполняться НЕ будет, тк до него был использован break
#     print("Пожалуй")
#     print("хватит")
# print(i)

''' Break лучше не использовать, тк в ООП нет такого понятия как break, его использование не явл правилом хорошего тона. лучше исп метод флажка - переменная flag, кот принимает значение true/false'''

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: 
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

''' 
Цикл for in - исп для ПЕРЕБОРА значений
'''

# for i in enumeration/перечисление:
#     operator 1
#     operator 2
#     ...
#     operator n

# for i in 1, -2, 3, 14, 5:
#     print(i) # программа поочередно будет выводить все значения - переменная i будет поочередно принимать значения

'''
ф-я range генерирует последовательность, принимает 3 аргумента: откуда начинаем (по умолчанию = 0), на каком числе заканчиваем, шаг (по умолчанию шаг = 1).
'''

'''
если в скобках указано только одно значение - будет генерироваться последовательность от 0 до указанного знач-я НЕ включая его
'''
# r = range(5) # 0 1 2 3 4

'''
если в скобках указаны два значения - с первого (включая его) - будет генерироваться последовательность до указанного знач-я НЕ включая его
'''
# r = range(2, 5) # 2 3 4
# r = range(0, -5) #ничего не будет выводиться, тк шаг по умолчанию 1
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# for i in range:
#     print(i) # 100 80 60 40 20

''' 
Цикл for также можно использовать для СТРОК
'''
# for i in "qwerty":
#     print(i)

# a = "qwerty"
# print(a[0])

# line = ""
# for i in range(5): # последовательность генерируется из 5 символов, значит цикл for будет выполняться 5 раз
#     line = "" # создаем пустую переменную line
#     for j in range(5):
#         line += "+" # к строке 5 раз прибавляем +
#     print(line) # 5 раз вывести строку, состоящую из 5 звездочек

''' 
СПИСКИ - тоже тип данных. list_1 = [] - создали пустой список.
ф-ии .lower, .upper, .replace
ф-я len позволяет узнать размер строки (и любой другой КОЛЛЕКЦИИ ДАННЫХ)
'''
# text = "СъЕШь еще этих мягких французских булок"
# print(text.lower()) # переведет все символы в нижний регистр
# print(text.upper()) # переведет все символы в верхний регистр
# print(text.replace('еще', 'ЕЩЕ')) # поменяет сочетание символов в строке - первым арг указываем ЧТО хотим изменить, вторым арг - НА ЧТО хотим изменить

'''
Срезы в СТРОКАХ
как и в массивах, в строках есть ИНДЕКСАЦИЯ - поэтому можно использовать срезы
'''
# text = "съешь еще этих мягких французских булок"
# print(text[0])
# print(text[1])
# print(text[len(text)-1]) # вывести последнюю букву - узнать кол-во символов в строке и отнять единицу, тк индексация начинается с нуля
# 47:00
# print(text[-1]) # тоже вывести последнюю букву
# print(text[-5]) # вывести 5-ю букву с конца
# print(text[:]) # вывести абсолютно все символы
# print(text[:2]) # вывести элементы с 0 индекса по 2-й индекс не включая его - похоже на ф-ю range
# print(text[len(text)-2:]) # возьмем всю длину строки -2 и выведем все, это символы #ок. То есть если после : не указываем число - выводятся символы до конца
# print(text[2:9]) # вывести элементы со 2-го по 9-й не включая его
# print(text[6:-18]) # вывести элементы с 6-го по 18-й с конца не включая его
# print(text[0:len(text):6]) # вывести элементы с 0-го до конца всей строки с шагом 6
# print(text[::6]) # если перед и после : не указывать ничего - будет выводиться все от начала до конца, эта строка тождественна строке выше
# print(text[2:9] + text[-5] + text[:2]) # элементы со 2-го по 9-й + 5-й с конца + с 0-го по 2-й не включая его


# .append(<...>) # добавить в конец
# .remove(<...>) # удалить элемент
# .del colors[0] # удалить элемент

'''
ЛЕКЦИЯ 2      ЛЕКЦИЯ 2       ЛЕКЦИЯ 2       ЛЕКЦИЯ 2       ЛЕКЦИЯ 2
'''
'''
Списки - list []
'''
# list_1 = [] #создали пустой список
# list_1 = list() #создали пустой список другим способом
# print(list_1) #вывести результат с пустым списком

# list_2 = [1, 2, 3, 4, 5] #создали список со значениями
# print(list_2) #вывести результат с заполненным списком
# print(*list_2) #вывести результат с заполненным списком без квадратных скобок []

#можем работать со списком с циклом for - перебирать значения
# for i in list_2:
#     print(i) #при каждой итерации i будет принимать поочередно значения из списка

# len можно использовать для любой коллекции данных
# print(len(list_2)) #выводится будет 4 - в списке 4 элемента

# можно обращаться к списку поэлементно - как и со строками, у списком нумерация начинается с 0
# print(list_2[0])
# print(list_2[-1]) #последний элемент списка, нумерация с конца

#добавление значения в список - ф-я .append
# list_2 = [1, 5]
# print(list_2)
# list_2.append(8) # в скобках () значение, которое хотим добавить ТОЛЬКО ОДИН АРГУМЕНТ
# print(list_2)

#заполним пустой список поочередно значениями 
# list_3 = []
# print(list_3)
# for i in range(5):
#     list_3.append(i)
#     print(list_3)

#удаление и возвращение последнего элемента ф-ей .pop
# list_4 = [12, 7, -1, 21, 0]
# print(list_4.pop()) #удаляет последний элемент и возвращает его без скобок []
# print(list_4) #если после вывести список - удаленного значения в нем не будет

# если укажем значение - это будет значение индекса удаляемого элемента
# print(list_4.pop(0))
# print(list_4) #если после вывести список - удаленного значения в нем не будет

# добавление элемента в список на нужную позицию - ф-я .insert
# принимает на вход два аргумента - позицию, на кот нужно вставить элемент
# и значение, которое нужно туда вставить, "подвинутый" элемент сдвинется вправо
# list_5 = [12, 7, -1, 21, 0]
# print(list_5.insert(2, 11))
# print(list_5)

# срезы в СТРОКАХ
# print(list_5[0]) # первый элемент
# print(list_5[1]) # второй элемент
# print(list_5[len(list_5)-1]) # вывести последний элемент - узнать кол-во символов в строке и отнять единицу, тк индексация начинается с нуля
# print(list_5[-1]) # тоже вывести последний элемент
# print(list_5[-5]) # вывести 5-й элемент с конца
# print(list_5[:]) # вывести абсолютно все символы
# print(list_5[:2]) # вывести элементы с 0 индекса по 2-й индекс не включая его
# print(list_5[len(list_5)-2:]) # возьмем всю длину строки -2 и выведем все это символы #ок. То есть если после : не указываем число - выводятся символы до конца
# print(list_5[2:9]) # вывести элементы со 2-го по 9-й не включая его
# print(list_5[6:-18]) # вывести элементы с 6-го по 18-й с конца не включая его
# print(list_5[0:len(list_5):6]) # вывести элементы с 0-го до конца всей строки с шагом 6
# print(list_5[::6]) # если перед и после : не указывать ничего - будет выводиться все от начала до конца, эта строка тождественна строке выше
# print(list_5[2:9] + list_5[-5] + list_5[:2]) # элементы со 2-го по 9-й + 5-й с конца + с 0-го по 2-й не включая его

'''
Кортеж - tuple () - неизменяемый список  - тоже тип данных. Защищает данные от изменений. Занимает МЕНЬШЕ места в ПАМЯТИ, работает БЫСТРЕЕ списков.
'''
# t = () #  создали пустой кортеж
# print(type(t))
# t = (1) # это НЕ кортеж - это int
# t = (1, 2, 3, ) # создали заполненный кортеж, в конце обязательно оставить ЗАПЯТУЮ

# список преобразуем в кортеж v = [1, 8, 9] v = tuple(v)
# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# ф-я множественное присваивание
# a = 1
# b = 2
# a, b = 1, 2
# a = b = 1

# разделим кортеж v = [1, 8, 9] на 3 переменные
# a, b, c = v # "распаковка" кортежа
# print (a, b, c)

# t = (1, 2, 3, 5)
# print(t[1])

# for i in t:
#     print(i) # вывести каждый элемент в списке 1-й способ

# for i in range(len(t)):
#     print(t[i])  # вывести каждый элемент в списке 2-й способ

# кортежи НЕ поддерживают ПРЕОБРАЗОВАНИЕ аргумента t[0] = 2 сделать нельзя

'''
Словарь - тоже тип данных. dictionary {} - неупорядоченная коллекция произвольных объектов с доступом по КЛЮЧУ (строка/число).
'''
# d = {} # создали словарь
# d = dict() # также создали ИЛИ преобразовали переменную в словарь

# d["q"] = "qwerty" # по ключу "q" - значение "qwerty"
# print(d)

# d["w"] = "werty" # по ключу "w" - значение "werty"
# print(d)

# print(d["q"]) # вывести значение словаря по ключу
# 21:40 время лекции, особенно 22:30 6 строка

'''
по Камянецкому:

dict_ = \       # вывести ключ-значение на разных строках
{
    'up' : '',
    'left' : '',
    'down' : '',
    'right' : '',
}

dict_[up] = 'down'
print(dict_[up]) # заменить значение 'up' на 'down'

set_ = frozenset(set_) замороженные мн-ва, добавление/удаление/изменение работать не будут

list_ = [for item in range(5)] # 5 раз в список добавим значение 
РАВНОСИЛЬНО
list_ = []
for item in range(5):
    list_.append(item)
print(list_) # 0 1 2 3 4


'''

'''
ЛЕКЦИЯ 3      ЛЕКЦИЯ 3       ЛЕКЦИЯ 3       ЛЕКЦИЯ 3       ЛЕКЦИЯ 3

Функции - специальные языковые конструкции (не тип данных).

Функции, модули, рекурсии, алгоритмы: быстрая сортировка и сортировка слиянием

Ф-я - def - фрагмент программы, используемый многократно.
Сколько АРГ ПЕРЕДАЕМ - столько и ПРИНИМАЕМ.
+
Сколько АРГ ПРИНИМАЕМ - столько ОТДАЕМ.

Ф-я может возвращать значения, может - не возвращать значения.
'''
# def function_name(x):
#     body line 1
#             ...
#     body line n
#     optional return

# Task 1: Create function sumNumbers(n), which will calculate the sum of all elements from 1 to n
def sumNumbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)

sumNumbers(5)

def sumNumbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum # если программа видит оператор return - завершает выполнение ф-ии

print(sumNumbers(5))

def sumNumbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

a = sumNumbers(5)
print(a)

def sumNumbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
    print("Stop") # поскольку ф-я завершила работу на return, print программа даже не подсвечивает, ф-я print не будет выполняться

a = sumNumbers(5)
print(a)

# Сколько АРГ ПЕРЕДАЕМ - столько и ПРИНИМАЕМ. Сколько АРГ ПРИНИМАЕМ - столько ОТДАЕМ.
def sumNumbers(n, y = "Hello"): # здесь по умолчанию присвоили аргументу y значение Hello, поэтому в строчке 507 при вызове ф-ии мы не передаем аргумент в переменную y.
    print(y)
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
    print("Stop") # поскольку ф-я завершила работу на return, print программа даже не подсвечивает, ф-я print не будет выполняться

a = sumNumbers(5) # но если есть необходимость - здесь можно задать новое значение переменной y - его и выведет программа
print(a)

# Task 2: Передать ф-ии мн-во букв и получить единое слово, но не известно, сколько будет букв - не знаем, сколько нужно передать аргументов.
# напишем ф-ю, которая будет ПРИНИМАТЬ НЕОГРАНИЧЕННОЕ КОЛ_ВО АРГ

def sumStr (*args): # через * показываем, что хотим передать неограниченное кол-во арг
    res = ""
    for i in args:
         res += i
    return res
print(sumStr("q", "e", "l"))
print(sumStr("q", "e", "l", "r", "f"))
# print(sumStr(1, 8, 9)) # произойдет ошибка, возможна работа только со строкой
print(sumStr("1, 8, 9"))

'''
Модульность. Повышает читаемость и понимание кода. Создаем несколько файлов - для ф-й по спискам, ф-й по кортежам, ф-й словарям и тп.
Модуль - файл, в кот находятся различные ф-ии, которые можем использовать. Т.е. в отдельном файле можно описать мн-во ф-й, а потом их использовать в программе.

*создали файл modul1.py, записали в него ф-ю maxCount*

Чтобы вызвать ф-ю из модуля, импортируем модуль - import modul1
Затем обратимся к модулю и укажем название ф-и, сразу передадим входные аргументы - print(modul1.maxCount(5, 9))

ИЛИ

Можно напрямую импортировать ф-ю: from modul1 import maxCount. В этом случае необязательно указывать название модуля, т. к. напрямую импортируем ф-ю

ИЛИ

Импортируем все ф-ии - from modul1 import *
'''
# import modul1 # название файла, где хранится модуль
# print(modul1.maxCount(5, 9))
# ИЛИ
# from modul1 import maxCount
# print(maxCount(10, 9))
# ИЛИ
# from modul1 import *
# print(maxCount(11, 9))

import modul1 as m1 # сокращаем название модуля на время действия работы нашей программы
print(m1.maxCount(2, 7))

'''
Рекурсия - ф-я, которая вызывает саму себя. 
При описании рекурсии нужно указать КОГДА ф-ии ОСТАНОВИТЬСЯ и перестать вызывать саму себя - указать БАЗИС РЕКУРСИИ.
'''

# task 3: Пользователь вводит число n и необходимо вывести n первых членов последовательности Фибоначчи.
# Последовательность Фибоначчи - каждое последующее число = сумме двух предыдущих. Первые два члена известны - это 0 и 1.

def fib(n):
    if n in [1, 2] : # это базис чтобы выходить из рекурсии
        return 1     # это базис чтобы выходить из рекурсии
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10) :
    list_1.append(fib(i))
print(list_1)

'''
Алгоритмы - набор инструкций для выполнения задачи. Любой фрагмент программного кода.
Рассмотрим алгоритмы сортировок:
Быстрая сортировка: разбивка большого на маленькое. Принцип действия - бинарный поиск.
Сортировка слиянием.
'''
# task 3: Друг загодывает число от 1 до 100, второй - пытается угадать.
# Алгоритм бинарного поиска - макс элементов делим на 2

def quickSort(array) :
    if len(array) <= 1 :
        return array
    else:
        pivot = array[0] #pivot - точка возврата
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))
# 25:00

'''
Сортировка слиянием. 
Принцип действия: список делим на 2, пока не останется по одному элементу.
Последовательность чисел НЕУПОРЯДОЧЕННАЯ после этого.
Из каждого элемента будем создавать теперь пару, которая имеет порядок от меньшего к большему.
'''
def mergeSort(nums):
    if len(nums):
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left) :
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right) :
            nums[k] = right[j]
            i += 1
            k += 1


'''
ЛЕКЦИЯ 4      ЛЕКЦИЯ 4       ЛЕКЦИЯ 4       ЛЕКЦИЯ 4       ЛЕКЦИЯ 4
Ф-ии высшего порядка, работа с файлами.

Анонимные ф-ии, lambda-ф-ии

Ф-ии высшего порядка map, filter, zip, enumerate
Модули для работы с папками os, shuyil
'''
# def f(x):
#     return x * x
# print(type(x)) # type(f) - <class function>

# def f(x):
#     return x * x
# a = f
# print(type(x)) #также type(f) - <class function>

# def f(x):
#     return x * x
# a = f
# print(a) # переименовали ф-ю f и задали ей новое имя. Точнее на определенный участок памяти в компьютере теперь ссылаются две переменные - f и a.
# a хранит в себе ссылку на ф-ю f, значит эти ссылки можно передавать в другие ф-ии.

# Создадим небольшой калькулятор
# def calk1(a):
#     return a + a
# def calk2(a):
#     return a * a
# def math(op, x):
#     print(op(x))

# math(calk1, 5)


# def calk1(a):
#     return a + b
# def calk2(a, b):
#     return a * b
# def math(op, x, y):
#     print(op(x, y))

# math(calk2, 5, 45)

# python - скриптовый язык, с помощью которого можно сильно сокращать код. Прим: генератор списков - в одну строчку.
# lambda ф-ии. 7:00


'''
ЛЕКЦИЯ 5      ЛЕКЦИЯ 5       ЛЕКЦИЯ 5       ЛЕКЦИЯ 5       ЛЕКЦИЯ 5

Google Colab(Jupyter). Знакомство с аналитикой.

Чтение и предварительный просмотр данных. Выбор данных. Простая статистика. Изображение статистических отношений. Линейные графики. Гистограммы. Точечные графики.

Аналитика: инструмент - Google Colab. Работа с табличными данными: инструмент - pandas.
Визуализация данных с помощью библиотек matplotlib и seaborn.

Перед машинным обучением: Проведение EDA(Exploratory Data Analyst) - разведочного анализа данных. Состоит в анализе основных св-в данных:
нахождении в них общих закономерностей, распределении и аномалий, построение начальных моделей, в т.ч. с исп инструментов визуализации.

Разведочный анализ данных - цели:
1) Максимальное "проникновение" в данные
2) Выявление осн структур
3) Выбор наиболее важных переменных
4) Обнаружение отклонений и аномалий
5) Проверка основных гипотез
'''
# импортируем библиотеку pandas, она может читать многие форматы, в т.ч. .csv, .xslx, .xls, .txt, .sql и др. - полный список тут - https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
# import pandas as pd # as(alias) - псевдоним, позволяет сократить названия библиотек до 2-х букв
# df = pd.read_csv('sample_data/california_housing_train.csv') # ф-я read_scv, в () - путь к файлу, который хочу прочитать
