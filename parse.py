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


def get_gen_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='col-9 tab-content')
    # with open('page.html', 'w') as file:
    #     file.write(items.prettify())
    year = items.find(string='Год ввода дома в эксплуатацию').find_parent('td').find_next().text.strip()
    floors = items.find(string='Количество этажей, ед.').find_parent('td').find_next().text.strip()
    updating = items.find(string='По данным Фонда ЖКХ информация последний раз актуализировалась:').find_parent('td').find_next().text.strip()
    series = items.find(string='Серия, тип постройки здания').find_parent('td').find_next().text.strip()
    type_of_building = items.find(string='Тип дома').find_parent('td').find_next_siblings()[-1].text.strip()
    emergency = items.find(string='Факт признания дома аварийным')
    if emergency is not None:
        emergency = emergency.find_parent('td').find_next_siblings()[-1].text.strip()
    cadastre = items.find(string='Кадастровый номер земельного участка')
    if cadastre is not None:
        cadastre = cadastre.find_parent('td').find_next_siblings()[-1].text.strip()
    floor = items.find(string='Стены и перекрытия. Тип перекрытий').find_parent('td').find_next_siblings()[-1].text.strip()
    walls = items.find(string='Стены и перекрытия. Материал несущих стен').find_parent('td').find_next_siblings()[-1].text.strip()
    print(year, floors, updating, series, type_of_building, emergency, cadastre, floor, walls)


def parse(query):
    # Получаем ссылку на запрашиваемый дом
    html_house = get_html(URL + SEARCH, query)
    if html_house.status_code == 200:
        links = get_links(html_house.text)
    else:
        print('Сайт не отвечает')
    if len(links) > 10:
        print('Слишком большая выборка, уточните данные о доме.')
        link = None
    else:
        link = links[0].replace('view', 'passport')

    # Получаем данные о доме
    if link is not None:
        html_gen_info = get_html(URL + link)
        if html_gen_info.status_code == 200:
            data = get_gen_info(html_gen_info.text)
        else:
            print('Сайт не отвечает')


query = [
    {'query': 'г. Санкт-Петербург, ул. Репищева, д. 21, к. 1'},
    {'query': 'край. Алтайский, г. Новоалтайск, ул. Белякова, д. 42'},
]

for i in query:
    parse(i)
