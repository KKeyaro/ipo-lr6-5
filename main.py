# Написать программу, которая:
# - Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
# - Находит количество положительных, отрицательных и нулевых элементов в списке.
# - Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
# - Выводит самое большое и самое маленькое значение

import random #Импорт модуля random 
numbers = [random.randint(-50, 50) for _ in range(25)] #Генерация списка
pos = sum(1 for n in numbers if n > 0) #Находим все положительные элементы
neg = sum(1 for n in numbers if n < 0) #Находим все отрицательные элементы
zero = sum(1 for n in numbers if n == 0) #Находим все нулевые элементы
pos_proc = (pos / 25) * 100 #Считаем процент положительных элементов
neg_proc = (neg / 25) * 100 #Считаем процент отрицательных элементов
zero_proc = (zero / 25) * 100 #Считаем процент нулевых элементов
maxn = max(numbers) #Находим максимальное значение
minn = min(numbers) #Находим минимальное значение
print(numbers) #Выводим все элементы
print("Положительные элементы: {pos} ({pos_proc}%)") #Выводим положительные элементы и их процент
print("Отрицательные элементы: {neg} ({neg_proc}%)") #Выводим отрицательные элементы и их процент
print("Нулевые элементы: {zero} ({zero_proc}%)") #Выводим нулевые элементы и их процент
print("Самое большое значение: {maxn}") #Выводим самое большое значение
print("Самое маленькое значение: {minn}") #Выводим самое маленькое значение
