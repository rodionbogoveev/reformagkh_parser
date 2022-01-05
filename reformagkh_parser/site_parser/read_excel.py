import openpyxl


def open_excel():
    data = openpyxl.open(r'test_data.xlsx', read_only=True)
    sheet = data.active
    for row in range(2, sheet.max_row + 1):
        row = sheet[row]
        region = row[2].value.split()
        region = region[0]
        settlement = row[4].value
        settlement_type = row[3].value
        if not settlement:
            settlement = None
        else:
            settlement = f'{settlement_type} {settlement}'
        street = row[6].value
        street_type = row[5].value
        if not street:
            street = None
        else:
            street = f'{street_type} {street}'
        house = f'д {row[7].value}'
        block = row[8].value
        if not block:
            block = None
        else:
            block = f'к {block}'
        address = f'{region} {settlement} {street} {house} {block}'
        query = {
            'region': region,
            'settlement': settlement,
            'street': street,
            'house': house,
            'block': block,
        }
        address = ''
        for i in query:
            if query[i]:
                address += f'{query[i]} '
        query['address'] = address

        with open('queryset.txt', 'a') as file:
            file.write(f'{query["address"]}\n')


open_excel()
