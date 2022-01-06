import sqlite3
import time

from create_result import create
from parse import parse

while True:
    conn = sqlite3.connect('reformagkh.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT MAX(id)
        FROM source
    """)

    last_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT *
        FROM result
        WHERE result.source_id = '%s'
    """ % last_id)

    result = cursor.fetchall()
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
    time.sleep(10)
