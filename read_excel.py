import openpyxl


A = 'г. Санкт-Петербург, ул. Репищева, д. 21, к. 1'


def open_excel():
    data = openpyxl.open('test_data.xlsx', read_only=True)
    sheet = data.active
    for row in range(2, sheet.max_row + 1):
    # for row in range(2, 5):
        row = sheet[row]
        region = row[2].value.split()
        if region[1].lower() == 'г':
            region_type = 'г.'
        elif 'респ' in region[1].lower():
            region_type = 'Респ.'
        elif 'обл' in region[1].lower():
            region_type = 'обл.'
        elif 'край' in region[1].lower():
            region_type = 'край.'
        region = region[0]
        # settlement = row[4].value if row[4].value is not None else ''
        # settlement_type = f' {row[3].value}' if row[3].value is not None else ''
        # settlement = settlement + settlement_type
        # street = str(row[6].value) if row[6].value != None else ''
        # street_type = f' {row[5].value}' if row[5].value is not None else ''
        # street = street + street_type
        # house = f'Дом {row[7].value}' if row[7].value is not None else ''
        # block = f' Корпус {row[8].value}' if row[8].value is not None else ''
        # house = str(house) + block
        query = {
            'region': f'{region_type} {region}',
            # 'settlement': settlement,
            # 'street': street,
            # 'house': house,
        }
        print(query)

open_excel()