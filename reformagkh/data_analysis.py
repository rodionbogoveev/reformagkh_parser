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
        SELECT COUNT(successful) AS cnt
        FROM result
        WHERE successful = 0
    """)
    unsuccessful = cursor.fetchone()[0]

    conn.close()
    return f'Всего объектов найдено: {successful}; не найдено: {unsuccessful}.'


if __name__ == "__main__":
    analysis()
