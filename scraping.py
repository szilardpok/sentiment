import requests
from bs4 import BeautifulSoup
import queries

def create_custom_telex(titles, leads):
    tx = []
    for idx, item in enumerate(titles):
        title = titles[idx].getText()
        href = titles[idx].get('href', None)
        try:
            lead = leads[idx].getText()
            tx.append({'title': title, 'href': 'https://telex.hu'+href, 'lead': lead})
        except IndexError:
            tx.append({'title': title, 'href': 'https://telex.hu' + href})
    return tx


def scrapetelex():
    print('kezdődik...')
    _PATH_ = "/Users/cx-ray/PycharmProjects/IntermediateProjects/WebScrape/db/pythonsqlite.db"

    res = requests.get('https://telex.hu')

    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.select('.item__title')
    leads = soup.select('.item__lead')

    txnews = create_custom_telex(titles, leads)

    placeholder = '**********************************************'

    for i in txnews:
        print(placeholder)
        values = (str(i['title']), str(i['href']))
        queries.add_news(_PATH_, values)
        print(i['title'])
        print(i['href'])
        try:
            print(i['lead'])
        except KeyError:
            continue
