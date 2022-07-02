import requests
from bs4 import BeautifulSoup


class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

# category = input('Введите категорию: ') # politics

html = requests.get(f'https://www.moscowtimes.ru/').text

soup = BeautifulSoup(html, 'html.parser')
#print(soup)

articles = soup.find_all('div', class_='article-excerpt-default')
#print(articles)
json_data = []
for article in articles:
    title = article.find('p', class_='article-excerpt-default__headline').get_text(strip=True)
    print(Style.MAGENTA + title)
    try:
        teaser = article.find('div', class_='article-excerpt-default__teaser').get_text(strip=True)
    except:
        teaser = 'Нет описания'
    print(Style.RED + teaser)

    image_link = article.find('img').get('data-src')
    print(image_link)
    json_data.append({
        'title': title,
        'teaser': teaser,
        'image_link': image_link
    })


import json
with open('news.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)


