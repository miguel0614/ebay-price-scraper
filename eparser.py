import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import pandas as pd


# Adds in search parameters
def format_url(name, sold, comp, low, high, condition):
    base_url = f"https://www.ebay.com/sch/i.html?from=R40&_nkw={name}&LH_Sold={sold}&LH_Complete={comp}&_ipg=200&_udlo={low}&_udhi={high}&LH_ItemCondition={condition}"
    print(base_url)
    return base_url


# Returns list of urls with page numbers
def generate_urls(url):
    urls = list()
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html5lib')
    try:
        urls = [url + "&_pgn=" + str(page_num) for page_num in
                range(1, int(soup.find_all("li", attrs={"class": "x-pagination__li"})[-1].text) + 1)]
    except IndexError:
        print("Only 1 Page of Results Available")
        urls.append(url)
    finally:
        return urls


# Gather website prices based on whether item status is sold or active
def scrape(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html5lib')
    if "&LH_Sold=1" in url:
        result = soup.find_all("span", attrs={"class": "POSITIVE"})
        parsed = [float(x.text.lstrip('$').replace(',', "")) for x in result if x.text[0] == '$']
    else:
        result = soup.find_all("span", attrs={"class": "s-item__price"})
        parsed = [float(x.text.lstrip('$').replace(',', "")) for x in result if x.text[0] == '$' and 'to' not in x.text]
    return parsed


# Returns list of prices from URL - Multi-threaded
def process_data(url):
    urls = generate_urls(url)
    with Pool(len(urls)) as p:
        data = p.map(scrape, urls)
    return [cost for page in data for cost in page]
