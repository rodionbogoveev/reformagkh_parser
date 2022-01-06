import sqlite3

while True:
    address = input(
        'Введите здесь адрес одной строкой, не указывая тип региона, например: '
        '"Санкт-Петербург, ул. Репищева, д. 21, к. 1" или "Краснодарский, '
        'г. Анапа, ул. Ленина, д. 134".\nЕсли вы хотите ввести адрес '
        'отдельными параметрами, то оставьте это поле пустым и нажмите Enter.\n'
        'Поле для ввода: '
    )
    print()
    if not address:
        print()
        region = input(
            'Введите название региона, не указывая его тип, '
            'например: "Татарстан", "Владимирская", "Москва".\n'
            'Поле для ввода: '
        )
        print()
        city = input(
            'Введите название населенного пункта, например: "г. Калининград", '
            '"пгт. Прохоровка", "д. Крюково".\n'
            'Поле для ввода: '
        )
        print()
        street = input(
            'Введите название улицы, например: "ул. Лесная", "пр-кт. Победы", '
            '"пер. Дорожный".\n'
            'Поле для ввода: '
        )
        print()
        house = input(
            'Введите номер дома, например: "д. 144", "д. 6В, к. 3".\n'
            'Поле для ввода: '
        )
        print()
        address = ''
        params = (region, city, street, house)
        for i in params:
            if i:
                address += f'{i} '
    else:
        region, city, street, house = None, None, None, None

    if not region and not city and not street and not house and not address:
        pass
    else:
        conn = sqlite3.connect('reformagkh.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO source (region, city, street, house, address)
            VALUES (?, ?, ?, ?, ?)
        """, (region, city, street, house, address))

        conn.commit()
        conn.close()
