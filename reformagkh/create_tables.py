import sqlite3


def create_db():
    """Создание базы данных."""
    conn = sqlite3.connect('reformagkh.db')
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS source (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            region varchar(64),
            city varchar(64),
            street varchar(64),
            house varchar(64),
            address varchar(200)
        );
        CREATE TABLE IF NOT EXISTS result (
            id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            year smallint unsigned CHECK (year >= 0),
            floors smallint unsigned CHECK (floors >= 0),
            updating date,
            series varchar(64),
            type_of_building varchar(64),
            emergency varchar(64),
            cadastre varchar(64),
            floor varchar(64),
            walls varchar(64),
            successful BOOLEAN NOT NULL CHECK (successful IN (0, 1)),
            source_id INTEGER,
            FOREIGN KEY(source_id) REFERENCES source(id)
        );
    """)

    conn.close()


if __name__ == '__main__':
    create_db()
