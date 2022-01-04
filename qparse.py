import openpyxl
import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


useragent = UserAgent()
options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', useragent.random)


query = {'region': 'Коми', 'settlement': 'Печора г', 'street': 'Печорский пр-кт', 'house': 'Дом 116'}



def main():
    driver = webdriver.Firefox(options=options)
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
        time.sleep(3)
        driver.find_elements_by_xpath("//*[@id='ui-id-3']")[0].click()
    
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
    
    # Поиск
    driver.find_elements_by_xpath("//button[contains(text(),'НАЙТИ')]")[0].click()

    # Переход по ссылке
    driver.find_elements_by_xpath("/html/body/section[2]/div/table/tbody/tr/td[1]/a")[0].click()
    
    # Переход на вкладку "Паспорт"
    driver.find_elements_by_xpath("/html/body/section[4]/div/a[1]")[0].click()
    
    # Конструктивные элементы дома
    driver.find_elements_by_xpath("//*[@id='constructive-tab']")[0].click()

    driver.close()
    return


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
        print(query)
        # main(query)


# open_excel()








# if __name__ == '__main__':
#     main()
