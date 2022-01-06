import openpyxl


def open_excel():
    data = openpyxl.open(r'test_data.xlsx', read_only=True)
    sheet = data.active
    for row in range(2, sheet.max_row + 1):
        row = sheet[row]
        region = row[2].value.split()
        region = region[0]
        city = row[4].value
        city_type = row[3].value
        if not city:
            city = None
        else:
            city = f'{city_type} {city}'
        street = row[6].value
        street_type = row[5].value
        if not street:
            street = None
        else:
            street = f'{street_type} {street}'
        house = f'д {row[7].value}'
        block = row[8].value
        if block:
            house = f'д {row[7].value} к {block}'
        address = f'{region} {city} {street} {house}'
        query = {
            'region': region,
            'city': city,
            'street': street,
            'house': house,
        }
        address = ''
        for i in query:
            if query[i]:
                address += f'{query[i]} '
        query['address'] = address

        with open('queryset.txt', 'a') as file:
            file.write(f'{query}\n')


open_excel()
