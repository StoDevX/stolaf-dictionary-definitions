#!/usr/bin/env python3
import requests
import unicodedata
import re
from bs4 import BeautifulSoup as Bs

def prettifyFilename(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def fetch():
    url_suffixes = ['a-g', 'h-o', 'p-z']
    url_base = 'https://wp.stolaf.edu/sa/'

    for page in url_suffixes:
        url = url_base + page
        print('getting', url)
        resp = requests.get(url)
        soup = Bs(resp.text, 'lxml')
        defs = soup.find_all(class_='t-content')[0]

        for term in defs:
            try:
                pretty = term.prettify()
                name = term.find('strong')
                if ((name is not None) is True):
                    # assuming we never have a word that is one character (handles the alphabet)
                    if(len(name) > 1):
                        name = prettifyFilename(name.get_text())
                        with open('./data/%s.html' % name, 'w', encoding='utf-8') as outfile:
                            outfile.write(pretty + '\n')
            except AttributeError:
                pass

if __name__ == '__main__':
    fetch()
