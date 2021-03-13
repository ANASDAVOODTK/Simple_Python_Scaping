import bs4, requests


res = requests.get('https://www.goldpriceindia.com/platinum-price-india.php')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('body > div:nth-child(3) > div > div:nth-child(1) > div.panel.panel-flp.plat > div.panel-body > table > tbody > tr:nth-child(2) > td')
elems1 = soup.select('body > div:nth-child(3) > div > div:nth-child(2) > div.panel.panel-flp.plat > div.panel-body > table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)')

print(elems[0].text + "   "+elems1[0].text)

