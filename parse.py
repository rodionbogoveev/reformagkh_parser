import requests
from bs4 import BeautifulSoup

URL = 'https://www.reformagkh.ru'
SEARCH = '/search/houses'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}


def get_html(url, query=None):
    html = requests.get(url, headers=HEADERS, params=query)
    return html


def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='text-dark')
    links = []
    for i in items:
        links.append(i.get('href'))
    return links

    # cars = []
    # for item in items:
    #     uah_price = item.find('span', class_='size15')
    #     if uah_price:
    #         uah_price = uah_price.get_text().replace(' • ', '')
    #     else:
    #         uah_price = 'Цену уточняйте'
    #     cars.append({
    #         'title': item.find('div', class_='na-card-name').get_text(strip=True),
    #         'link': HOST + item.find('span', class_='link').get('href'),
    #         'usd_price': item.find('strong', class_='green').get_text(),
    #         'uah_price': uah_price,
    #         'city': item.find('svg', class_='svg_i16_pin').find_next('span').get_text(),
    #     })
    # return cars


def get_general_information():
    pass


def parse(query):
    # Получаем ссылку на запрашиваемый дом
    html_house = get_html(URL + SEARCH, query)
    if html_house.status_code == 200:
        links = get_links(html_house.text)
    else:
        print('Сайт не отвечает')
    if len(links) > 10:
        print('Слишком большая выборка, уточните данные о доме.')
    else:
        link = links[0]

    # Получаем данные о доме
    html_gen_info = get_html(URL + link)


query = {'query': 'г. Санкт-Петербург, ул. Репищева, д. 21, к. 1'}
parse(query)
