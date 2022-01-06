import sqlite3

conn = sqlite3.connect('reformagkh.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE source(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        region varchar(64) NOT NULL, 
        city varchar(64) NOT NULL, 
        street varchar(64) NOT NULL, 
        house varchar(64) NOT NULL
    );
""")
c.execute("""
    CREATE TABLE result(
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        year smallint unsigned NOT NULL CHECK (year >= 0), 
        floors smallint unsigned NOT NULL CHECK (floors >= 0), 
        updating date NOT NULL, 
        series varchar(64) NOT NULL, 
        type_of_building varchar(64) NOT NULL, 
        emergency varchar(64) NOT NULL, 
        cadastre varchar(64) NOT NULL, 
        floor varchar(64) NOT NULL, 
        walls varchar(64) NOT NULL, 
        source_id INTEGER, 
        FOREIGN KEY(source_id) REFERENCES source(id)
    );
""")
conn.commit()
c.close()