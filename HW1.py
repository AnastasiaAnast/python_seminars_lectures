# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input("Введите трехзначное число: "))
firstNum : int = num % 10
print(firstNum)
secondNum : int = num // 10 % 10
print(secondNum)
thirdNum : int = num // 100  % 10
print(thirdNum)
sum = firstNum + secondNum + thirdNum
print(f"Сумма цифр этого трехзначного числа = {sum}")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# 2 2 8    12
# 3 3 12   18
# 5 5 20   30
# 6 6 24   36
# 7 7 28   42
# 8 8 32   48
# 9 9 36   54

print("Петя и Сережа сделали одинаковое кол-во журавликов, а Катя - в 2 раза больше, чем Петя и Сережа вместе.")
allCranes = int(input("Введите кол-во журавликов, которое сделали все дети, например 6, 12, 18, 24 или любое другое, кратное 6: "))
if allCranes % 6 == 0:
    katyasCranes = allCranes // 3 * 2
    serezhasCranes = katyasCranes // 2
    petyasCranes = katyasCranes // 2
    print(f"Катя сделала {katyasCranes} журавликов, Сережа - {serezhasCranes}, а Петя - {petyasCranes}")
else:
    print("Введенное число не может быть использовано в данной задаче.")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
#  и получали билет с номером. Счастливым билетом называют такой 
# билет с шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
# Решение через массив, индекс

numOfTicket = input("Проверим, является ли Ваш билет счастливым - введите его шестизначный номер: ")
if len(numOfTicket) == 6:
    if int(numOfTicket[0]) + int(numOfTicket[1]) + int(numOfTicket[2]) == int(numOfTicket[3]) + int(numOfTicket[4]) + int(numOfTicket[5]):
        print("Ура! У Вас действительно счастливый билет!")
    else:
        print("Увы, пока это просто билет, в следующий раз точно повезет!")
else:
    print("Вы ввели не шестизначное число")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

print("Можно ли от шоколадки размером n*m долек отломить k долек, если разрешается разломить шоколадку только на два прямоугольника?")
n = int(input("Введите кол-во долек шоколадки в длину: "))
m = int(input("Введите кол-во долек шоколадки в ширину: "))
k = int(input("Введите кол-во долек, которое хотите отломить: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Можно")
else:
    print("Нельзя")