#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as Bs

def fetch():
    url_suffixes = ['a-g', 'h-o', 'p-z']
    url_base = 'https://wp.stolaf.edu/sa/'

    for page in url_suffixes:
        url = url_base + page
        print('getting', url)
        resp = requests.get(url)
        soup = Bs(resp.text, 'lxml')
        defs = soup.find_all(class_='t-content')[0]
        pretty = defs.prettify()
        with open('./data/%s.html' % page, 'w', encoding='utf-8') as outfile:
            outfile.write(pretty + '\n')

if __name__ == '__main__':
    fetch()
