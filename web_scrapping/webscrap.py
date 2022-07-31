# get items from ebay and other ecommerce stores

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=baby+stroller&_sacat=0&LH_TitleDesc=0&Type=Buggy%7CLightweight%2520Buggy&Age%2520Suitability=From%2520Birth&_dcat=66700&LH_PrefLoc=1&LH_Auction=1&rt=nc&LH_Sold=1&LH_Complete=1"

# function: extract, transform, load


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    feedback = soup.find_all('div', {'class': 's-item__info clearfix'})
    strollerslist = []
    print(len(feedback))
    for item in feedback:
        baby_strollers = {
            'title': item.find('h3', {'class': 's-item__title'}).text,
            'price_sold': item.find('span', {'class': 's-item__price'}).text.replace('£', '').strip(),
            # 'date_sold': item.find('span', {'class': 's-item__title--tagblock__COMPLETED'}).find('span', {'class': 'POSITIVE'}).text,
            # 'bids': item.find('span', {'class': 's-item__bids'}).text,
            'link': item.find('a', {'class': 's-item__link'})['href'],

        }
        strollerslist.append(baby_strollers)
        # print(baby_strollers)
    return strollerslist


def output(strollerslist):
    strollersdf = pd.DataFrame(strollerslist)
    strollersdf.to_csv('output_copy.csv', index=False)
    print("saved to CSV")
    return


soup = get_data(url)
strollerslist = parse(soup)
output(strollerslist)



o = open('test.txt', 'w')

o.write('Hello World')

o.close()

for num in range(10):
    print(num)
