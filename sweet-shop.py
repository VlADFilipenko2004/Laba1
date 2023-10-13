sweet_shop = {"Торт": [["Вишня, крем, сахар, мука"], 6, 150],
              "Пирожное": [["Крем"], 4, 100],
              "Маффин": [["Нежное тесто"], 3, 85]}

print('\t\tМеню: \nОписание - 1\nЦена - 2\nКоличество - 3\nВся информация - 4\nПокупка - 5\nВыход - 6')

while True:
    number = (input('Ваш выбор: '))

    if number == "1":
        for key, value in sweet_shop.items():
            print(key, '-', ','.join(value[0]))

    elif number == "2":
        for key, value in sweet_shop.items():
            print(key, f'- {value[1]}$ за 1 шт.')

    elif number == "3":
        for key, value in sweet_shop.items():
            print(key, f'- {value[2]} шт.')

    elif number == "4":
        for key, value in sweet_shop.items():
            print(f'\n {key}', '\nСостав:', ",".join(value[0]),
                  f'\nЦена: {value[1]}$ за 1 шт.', f'\nКоличество: {value[2]} шт.')

    elif number == "5":
        try:
            cost = 0
            while True:
                buy = input('Что вы хотите купить? "Торт", "Пирожное", "Маффин" или '
                            'введите n для завершения покупок: ')
                if buy == 'n':
                    break
                amount = float(input('Сколько штук вы хотите купить? '))
                if amount > sweet_shop[buy][2]:
                    print("К сожалению, данный товар ограничен, выберите другое количество или товар")
                    continue
                cost += amount * sweet_shop[buy][1]
                sweet_shop[buy][2] -= amount
            print(f"С вас {cost} $.")
        except ValueError:
            print("Неверный тип данных!")

    elif number == "6":
        print("Спасибо, что зашли в наш магазин! До свидания!")
        break
    else:
        print("Неизвестная команда! Попробуйте еще раз")