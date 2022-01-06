import sqlite3


def analysis():
    """Функция анализа таблицы result."""
    conn = sqlite3.connect('reformagkh.db')
    cursor = conn.cursor()

    # Получаем количество найденных объектов
    cursor.execute("""
        SELECT COUNT(successful) AS cnt
        FROM result
        WHERE successful = 1
    """)
    successful = cursor.fetchone()[0]

    # Получаем количество не найденных объектов
    cursor.execute("""
        SELECT COUNT(successful)
        FROM result
        WHERE successful = 0
    """)
    unsuccessful = cursor.fetchone()[0]

    # Получаем количество объектов для "Материал несущих стен: Кирпичный"
    cursor.execute("""
        SELECT DISTINCT COUNT(region) AS cnt, region
        FROM source
        WHERE id IN
            (SELECT source_id
            FROM result
            WHERE walls LIKE '%ирпич%')
        GROUP BY region
    """)
    bricks = cursor.fetchall()

    print(f'Всего объектов найдено: {successful}. Не найдено: {unsuccessful}.')
    print('Количество объектов для "Материал несущих стен: Кирпичный"'
          ' по каждому региону: ')
    for i in bricks:
        print(f'{i[1]}: {i[0]}.')

    # Получаем максимальную этажность для каждого материала несущих стен
    # в каждом городе
    cursor.execute("""
        SELECT DISTINCT(city) FROM source WHERE city <> ''
    """)
    cities = cursor.fetchall()
    for i in cities:
        cursor.execute(
            f"SELECT DISTINCT(walls), MAX(floors) FROM result WHERE source_id "
            f"IN (SELECT id FROM source WHERE city = '{i[0]}')")
        wall = cursor.fetchall()
        if wall[0][0] and wall[0][1]:
            print(
                f'В населенном пункте "{i[0]}" для "Материал несущих стен: '
                f'{wall[0][0]}" максимальная этажность - {wall[0][1]}.'
            )
    print()

    conn.close()


if __name__ == "__main__":
    analysis()
