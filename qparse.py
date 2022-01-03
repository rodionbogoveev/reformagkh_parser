import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def get_region(driver):
    driver.find_element_by_name('region').send_keys(input('Введите регион: '))
    time.sleep(1)
    regions = driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li/div")
    return regions


def main():
    trying = 3
    driver = webdriver.Firefox()
    driver.get('https://www.reformagkh.ru/search/houses-advanced')
    while trying != 0:
        regions = get_region(driver)
        if len(regions) == 0:
            trying += -1
            print('\nПо вашему запросу регион не найден.\n')
            driver.find_element_by_name('region').clear()
        else:
            trying = 0
            regions[0].click()

    time.sleep(10)

    driver.close()


def open_excel():
    data = openpyxl.open('test_data.xlsx', read_only=True)
    sheet = data.active
    for row in range(2, sheet.max_row + 1):
        row = sheet[row]
        region = row[2].value.split()[0]
        settlement = row[4].value if row[4].value is not None else ''
        settlement_type = f' {row[3].value}' if row[3].value is not None else ''
        settlement = settlement + settlement_type
        street = str(row[6].value) if row[6].value != None else ''
        street_type = f' {row[5].value}' if row[5].value is not None else ''
        street = street + street_type
        house = f'Дом {row[7].value}' if row[7].value is not None else ''
        block = f' Корпус {row[8].value}' if row[8].value is not None else ''
        house = str(house) + block
        query = {
            'region': region,
            'settlement': settlement,
            'street': street,
            'house': house,
        }
        print(query)

open_excel()








# if __name__ == '__main__':
#     main()
