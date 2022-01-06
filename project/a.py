import sqlite3

conn = sqlite3.connect('data.db')

# f = {
#     'region': 'Санкт-Петербург',
#     'city': '',
#     'street': 'ул Репищева',
#     'house': 'д 21 к 1',
#     'address': 'Санкт-Петербург ул Репищева д 21 к 1 '
# }
a = {'region': 'Комя',
    'city': 'Печора г',
    'street': 'Печорский пр-кт',
    'house': 'Дом 116'}

# Source.objects.create(
#     region=f['region'],
#     city=f['city'],
#     street=f['street'],
#     house=f['house'],
#     )

c = conn.cursor()
# c.execute("""
#     INSERT INTO site_parser_source (region, city, street, house) 
#     VALUES (?, ?, ?, ?)
#     """, (a['region'], a['city'], a['street'], a['house']))
# conn.commit()
c.execute("SELECT * FROM site_parser_source")
items = c.fetchall()
for i in items:
    for f in i:
        print(f, end='')
    print()

conn.close()