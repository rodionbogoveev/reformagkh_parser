import sqlite3


def analysis():
    conn = sqlite3.connect('reformagkh.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(successful) AS cnt
        FROM result
        WHERE successful = 1
    """)
    successful = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(successful)
        FROM result
        WHERE successful = 0
    """)
    unsuccessful = cursor.fetchone()[0]

    cursor.execute("""
        SELECT DISTINCT COUNT(region) AS cnt, region
        FROM source
        WHERE id IN
            (SELECT source_id
            FROM result
            WHERE walls LIKE '%ирпич%')
        GROUP BY region
    """)
    items = cursor.fetchall()

    print(f'Всего объектов найдено: {successful}. Не найдено: {unsuccessful}.')
    print('Количество объектов для "Материал несущих стен: Кирпичный" по каждому региону: ')
    for i in items:
        print(f'{i[1]}: {i[0]}.')

    cursor.execute("""
        SELECT DISTINCT(city) FROM source WHERE city <> ''
    """)
    cities = cursor.fetchall()
    for i in cities:
        cursor.execute(f"SELECT DISTINCT(walls), MAX(floors) FROM result WHERE source_id IN (SELECT id FROM source WHERE city = '{i[0]}')")
        wall = cursor.fetchall()
        print(
            f'В населенном пункте "{i[0]}" для "Материал несущих стен: {wall[0][0]}" максимальная этажность - {wall[0][1]}.'
        )
    print()

    conn.close()


if __name__ == "__main__":
    analysis()
