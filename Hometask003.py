# Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение
# второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим,
# если из последовательности удалить наибольший элемент.
# Пример:
# 1
# 7
# 9
# 0
# Вывод:
# 7

numbers = [1, 7, 9, 0]

max_number = numbers[0]
for i in numbers:
    if i > max_number:
        max_number = i

numbers.remove(max_number)

max_number = numbers[0]
for i in numbers:
    if i > max_number:
        max_number = i

print(f'Второй по величине элемент = {max_number}')