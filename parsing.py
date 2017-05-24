import urllib.request
from bs4 import BeautifulSoup

base_url = input('Enter base url: ')

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_page_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', class_='r_carousel1')
    chapters = content.find_all('a', class_='line')
    return len(chapters)

def parse_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', class_='r_carousel1')
    chapter_titles = content.find_all('a', class_='line')
    chapter_title = []
    for i in chapter_titles:
        title_i = 'Глава' + i.text[12:]
        chapter_title.append(title_i)
    chapter_title.reverse()
    return chapter_title

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    ch_content = soup.find('div', class_='text')
    return ch_content.text

chapter_content = []

chapter_title = parse_title(get_html(base_url))

page_count = get_page_count(get_html(base_url))

for page in range(1, page_count):
    html = parse(get_html(base_url + '/ru/' + '%d' % page))
    chapter_content.append(html)

with open('ranobe.txt', 'w') as f:
    i = 0
    while i < page_count:
        f.write(chapter_title[i] + '\n\n')
        f.write('\t' + chapter_content[i] + '\n\n')
        i += 1
    print('Done!')