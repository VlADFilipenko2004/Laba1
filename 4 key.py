dict_0 = dict(k2='Ri', k1='Nihao', k4='Ferstday', k3='Goodby', k5 ='Hi!')
print("Изначальный словарь: ", dict_0.items())
dict_1 = dict(sorted(dict_0.items()))
print("Отсортированный словарь по возрастанию: ", dict_1.items())
dict_others = dict()

while len(dict_1) > 0:
    dict_others.update([dict_1.popitem()])
print("Отсортированный словарь по убыванию: ", dict_others.items())

#max_key = max(dict_0)
max_key = max(dict_0, key=dict_0.get)
print("Максимальное значение слова в словаре: ", dict_others.get(max_key))