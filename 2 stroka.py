import re

S = str(input("Введите строку из слов для выполнения задания\n"))
Sr= re.sub(r"\d+", "", S)
print("Ваша строка без цифр: ", Sr)
# S=S.strip([S])    #Удаление пробельных символов в начале и в конце строки

kmax = 0
k1 = 0
i = 1
kol = Sr.split()
spis = Sr.split(' ');
while i < len(spis):
    if len(spis[i]) > k1:
        k1 = len(spis[i])
        kmax = i
    i += 1


print("Количество слов: ", len(kol))
print("Самое длинное слово: ", spis[kmax])