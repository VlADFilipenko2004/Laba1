import re

s = "Привет, мир!"
result = re.sub("\\w+", "", s)
print(result)  # -> "", т.е. строка без слов

n = int(input("Введите количество чисел для ввода: "))

сначало нужно рассмотреть как строку значения, затем удалить оттуда все буквенные обозначения,
после преобразовать чисто полученныую строку с цифрами в int
Добавить условие, если после чистки строки останется только пустая строка

print("Теперь введите числа для списка:")

i = 0
list = []
while i < n:
    a = int(input())
    здесь тоже самое воспроизвести
    list.append(a)
    i += 1
i = 0
result_list = []
while i < n - 1:
    # a=int(input())
    b = int(list[i] + list[i + 1])
    result_list.append(b)
    i += 1
print("Изначальный список: ", list)
print("Решение: ", result_list)
