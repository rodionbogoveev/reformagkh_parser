import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


query = {
    'region': 'Санкт-Петербург',
    'settlement': '',
    'street': 'Репищева ул',
    'house': 'Дом 21 Корпус 1'
}

# query = {
#     'region': 'Калмыкия', 
#     'settlement': 'Большой Царын п', 
#     'street': 'С.Убушиева ул', 
#     'house': 'Дом 9'
# }



def main():
    driver = webdriver.Firefox()
    driver.get('https://www.reformagkh.ru/search/houses-advanced')

    # Ввод региона
    driver.find_element_by_name('region').send_keys(query['region'])
    time.sleep(1)
    driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li/div")[0].click()

    # Ввод населенного пункта
    if not query['settlement']:
        pass
    else:
        driver.find_element_by_name('settlement').send_keys(query['settlement'])
        time.sleep(1)
        driver.find_elements_by_xpath("//ul[@id='ui-id-3']/li/div")[0].click()
    
    # Ввод улицы
    driver.find_element_by_name('street').send_keys(query['street'])
    time.sleep(1)
    if not query['settlement']:
        driver.find_elements_by_xpath("//ul[@id='ui-id-3']/li/div")[0].click()
    else:
        driver.find_elements_by_xpath("//ul[@id='ui-id-7']/li/div")[0].click()
    
    # Ввод дома
    driver.find_element_by_name('house').send_keys(query['house'])
    time.sleep(1)
    if not query['settlement']:
        driver.find_elements_by_xpath("//ul[@id='ui-id-4']/li/div")[0].click()
    else:
        driver.find_elements_by_xpath("//ul[@id='ui-id-8']/li/div")[0].click()
    
    driver.find_elements_by_xpath("//button[contains(text(),'НАЙТИ')]")[0].click()
    time.sleep(5)

    driver.close()


main()


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

open_excel()








# if __name__ == '__main__':
#     main()
