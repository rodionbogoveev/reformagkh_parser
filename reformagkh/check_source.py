import sqlite3
import time

from create_result import create
from parse import parse


def check():
    """Функция опрашивания таблицы source на появление новой записи."""
    while True:
        conn = sqlite3.connect('reformagkh.db')
        cursor = conn.cursor()

        # Получаем id последней записи в таблице source
        cursor.execute("""
            SELECT MAX(id)
            FROM source
        """)
        last_id = cursor.fetchone()[0]

        # Проверяем, есть ли запись в таблице result с таким source_id
        cursor.execute("""
            SELECT *
            FROM result
            WHERE result.source_id = '%s'
        """ % last_id)
        result = cursor.fetchall()

        # Если записи нет, то отправляем ее в функцию parse.
        # Если есть, то ничего не делаем.
        if not result:
            cursor.execute("""
                SELECT *
                FROM source
                WHERE id = '%s'
            """ % last_id)
            query = cursor.fetchone()
            if not query:
                pass
            else:
                query = query[-1]
                print(f'Отправляю на парсинг новые данные: "{query}".')
                trying = 0
                # Делаем 3 попытки на получение данных. Если данные получить
                # не удалось, то делаем запись в таблице result с пометкой,
                # что попытка неудачная
                while trying <= 3:
                    data = parse(query)
                    trying += 1
                    if data:
                        print('Данные получены.')
                        data['successful'] = 1
                        create(data, last_id)
                        trying = 4
                    elif not data and trying == 3:
                        print(f'Данные не получены, попытка - {trying}')
                        data = {
                                'year': None,
                                'floors': None,
                                'updating': None,
                                'series': None,
                                'type_of_building': None,
                                'emergency': None,
                                'cadastre': None,
                                'floor': None,
                                'walls': None,
                                'successful': 0
                        }
                        create(data, last_id)
                        trying += 1
                    else:
                        print(f'Данные не получены, попытка {trying}.\n')
                    time.sleep(10)

        conn.close()
        # Опрашиваем базу данных каждые 10 секунд
        time.sleep(10)


if __name__ == '__main__':
    check()
