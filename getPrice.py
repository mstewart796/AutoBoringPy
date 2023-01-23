import bs4, requests

def getPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#s0-0-19-5-11-26-50 > div > span.item-price > div')
    return elems[0].text

price = getPrice('https://www.ebay.co.uk/p/27041987087?iid=185463083149')
print('The price is ' + price)
