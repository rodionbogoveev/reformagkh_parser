import openpyxl


A = 'г. Санкт-Петербург, ул. Репищева, д. 21, к. 1'


def open_excel():
    data = openpyxl.open('test_data.xlsx', read_only=True)
    sheet = data.active
    for row in range(2, sheet.max_row + 1):
    # for row in range(2, 10):
        row = sheet[row]
        region = row[2].value.split()
        # if region[1].lower() == 'г':
        #     region_type = 'г.'
        # elif 'респ' in region[1].lower():
        #     region_type = 'Респ.'
        # elif 'обл' in region[1].lower():
        #     region_type = 'обл.'
        # elif 'край' in region[1].lower():
        #     region_type = 'край.'
        # region = f'{region_type} {region[0]}'
        region = region[0]
        settlement = row[4].value
        settlement_type = row[3].value
        # if settlement_type:
        #     settlement_type += '.'
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
        # street = street + street_type
        house = f'д {row[7].value}'
        block = row[8].value
        if not block:
            block = None
        else:
            block = f'к {block}'
        query = {
            'region': region,
            'settlement': settlement,
            'street': street,
            'house': house,
            'block': block,
        }
        for i in query:
            if query[i]:
                print(query[i], end=' ')
        print()

open_excel()