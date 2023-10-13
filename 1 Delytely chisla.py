flag = 0
while flag == 0:
    a = int(input("Введите натуральное число: "))
    if a < 1:
        print('Вы ввели не натуральное число. Введите заново натуральное число')
    else:
        flag = 1

i = 1
print('Делители числа ', a, ' равны:')
while i < a + 1:
    if a % i == 0:
        print(i)
    i += 1

# print(a)
