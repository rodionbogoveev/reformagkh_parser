import sqlite3

from data_analysis import analysis


def create(data, last_id):
    """Функция создания записи в таблице result."""
    conn = sqlite3.connect('reformagkh.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO result (
            year, floors, updating, series, type_of_building, emergency,
            cadastre, floor, walls, successful, source_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data['year'], data['floors'], data['updating'], data['series'],
        data['type_of_building'], data['emergency'], data['cadastre'],
        data['floor'], data['walls'], data['successful'], last_id
    ))

    conn.commit()
    conn.close()

    print('Данные записаны.\n')
    analysis()
    return
