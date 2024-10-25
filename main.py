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
print(f"Положительные элементы: {pos} ({pos_proc}%)") #Выводим положительные элементы и их процент
print(f"Отрицательные элементы: {neg} ({neg_proc}%)") #Выводим отрицательные элементы и их процент
print(f"Нулевые элементы: {zero} ({zero_proc}%)") #Выводим нулевые элементы и их процент
print(f"Самое большое значение: {maxn}") #Выводим самое большое значение
print(f"Самое маленькое значение: {minn}") #Выводим самое маленькое значение