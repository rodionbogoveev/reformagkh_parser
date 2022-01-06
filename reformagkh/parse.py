from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = 'https://www.reformagkh.ru'
HEADERS = {'user-agent': UserAgent().random, 'accept': '*/*'}


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


def get_gen_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='col-9 tab-content')
    year = items.find(string='Год ввода дома в эксплуатацию')
    if year:
        year = year.find_parent('td').find_next().text.strip()
    floors = items.find(string='Количество этажей, ед.')
    if floors:
        floors = floors.find_parent('td').find_next().text.strip()
    updating = items.find(
        string='По данным Фонда ЖКХ информация последний раз '
               'актуализировалась:'
    )
    if updating:
        updating = updating.find_parent('td').find_next().text.strip()
    series = items.find(string='Серия, тип постройки здания')
    if series:
        series = series.find_parent('td').find_next().text.strip()
    type_of_building = items.find(string='Тип дома')
    if type_of_building:
        type_of_building = type_of_building.find_parent(
            'td'
        ).find_next_siblings()
        type_of_building = type_of_building[-1].text.strip()
    emergency = items.find(string='Факт признания дома аварийным')
    if emergency:
        emergency = emergency.find_parent('td')
        emergency = emergency.find_next_siblings()[-1].text.strip()
    cadastre = items.find(string='Кадастровый номер земельного участка')
    if cadastre:
        cadastre = cadastre.find_parent('td').find_next_siblings()
        cadastre = cadastre[-1].text.strip()
    floor = items.find(string='Стены и перекрытия. Тип перекрытий')
    if floor:
        floor = floor.find_parent('td').find_next_siblings()[-1].text.strip()
    walls = items.find(string='Стены и перекрытия. Материал несущих стен')
    if walls:
        walls = walls.find_parent('td').find_next_siblings()[-1].text.strip()
    data = {
        'year': year,
        'floors': floors,
        'updating': updating,
        'series': series,
        'type_of_building': type_of_building,
        'emergency': emergency,
        'cadastre': cadastre,
        'floor': floor,
        'walls': walls,
    }
    return data


def parse(query):
    # Получаем ссылку на запрашиваемый дом
    a = quote(query)
    html_house = get_html(f'https://www.reformagkh.ru/search/houses?query={a}')
    if html_house.status_code == 200:
        links = get_links(html_house.text)
    else:
        print('Сайт не отвечает.')
    if len(links) > 10:
        print('Слишком большая выборка, уточните данные о доме.')
        link = None
    elif not links:
        print('По заданному адресу не найдено ни одного дома.')
        link = None
    else:
        link = links[0].replace('view', 'passport')
    # Получаем данные о доме
    if link:
        html_gen_info = get_html(URL + link)
        if html_gen_info.status_code == 200:
            data = get_gen_info(html_gen_info.text)
            return data
        else:
            print('Сайт не отвечает.')
            return
    else:
        print('Не удалось получить данные о доме.')
        return
