import requests
from bs4 import BeautifulSoup


# url = "https://www.ebay.com/sch/i.html?from=R40&_nkw={}&LH_Sold=1&LH_Complete=1&_ipg=200&_pgn=1".format(input("Input Search Parameter: "))


def find_sold(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    ret = []
    try:
        for page in range(int(soup.find_all("li", attrs={"class": "x-pagination__li"})[-1].text)):
            result = soup.find_all("span", attrs={"class": "POSITIVE"})
            data = [float(x.text.lstrip('$').replace(',', "")) for x in result if x.text[0] == '$']
            ret.extend(data)

    except IndexError:
        result = soup.find_all("span", attrs={"class": "POSITIVE"})
        data = [float(x.text.lstrip('$').replace(',', "")) for x in result if x.text[0] == '$']
        ret.extend(data)
    finally:
        return ret


def find_current(url):
    pass


def format_url():
    pass


print(len(find_sold("https://www.ebay.com/sch/i.html?from=R40&_nkw=iphone+8&LH_Sold=1&LH_Complete=1&_ipg=200&_pgn=1&LH_ItemCondition=1000&_udlo=500&_udhi=1000")))
