#made by @slay_the_normies
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
response = http.request('GET', 'https://coinmarketcap.com/')
soup = BeautifulSoup(response.data,features="lxml")  # Note the use of the .data property
soup= str(soup)
print(len(soup))
if 409736>len(soup):
    print('small')
    current_ethprice_int=soup.find('data-eth="')
    #print(current_ethprice_int)
    eth_price=soup[current_ethprice_int+10:current_ethprice_int+16]
    eth_prices=float(eth_price.replace('"',''))
    btc_prices=soup[soup.find('" data-byn="')-13:soup.find('" data-byn="')-1]
    btc_prices=(btc_prices.replace('"',''))
    btc_prices=float(btc_prices.replace('=',''))
    btc_24h=soup[soup.find('data-btc24h="')+13:soup.find('data-btc24h="')+21]
    btc_24h=(btc_24h.replace('"',''))
    btc_24h=(btc_24h.replace(' ',''))
    btc_24h=float(btc_24h.replace('d',''))
    eth_24h=soup[soup.find('data-eth24h="')+13:soup.find('data-eth24h="')+21]
    eth_24h=(eth_24h.replace('"',''))
    eth_24h=(eth_24h.replace(' ',''))
    eth_24h=float(eth_24h.replace('d',''))
    print(btc_prices, 'bitcoin price')
    print(eth_prices, 'ethereum price')
    print(btc_24h, '24h btc change')
    print(eth_24h, '24h eth change')

else:
    print('big')
    btc=soup[soup.find('Bitcoin'):]
    btc=btc[btc.find('Bitcoin'):-300000]
    btc_prices=btc
    btc_prices=btc_prices[btc_prices.find('markets">$'):]
    btc_prices=btc_prices[10:btc_prices.find('<')]
    btc_prices=btc_prices.replace(',','')
    btc=btc[btc.find('sort-by__percent-change-24-h"><div')+34:]
    btc=btc[:btc.find('</div>')-1]
    btc=btc[btc.find('">')+2:]
    btc_24h=float(btc)
    eth=soup[soup.find('Ethereum'):]
    eth=eth[eth.find('Ethereum'):-300000]
    eth_prices=eth
    eth_prices=eth_prices[eth_prices.find('markets">$'):]
    eth_prices=eth_prices[10:eth_prices.find('<')]
    eth_prices=eth_prices.replace(',','')
    eth_prices=float(eth_prices)
    eth=eth[eth.find('sort-by__percent-change-24-h"><div')+34:]
    eth=eth[:eth.find('</div>')-1]
    eth=eth[eth.find('">')+2:]
    eth_24h=float(eth)
    print(btc_prices, 'bitcoin price')
    print(eth_prices, 'ethereum price')
    print(btc_24h, '24h btc change')
    print(eth_24h, '24h eth change')
'''
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
response = http.request('GET', 'https://www.coingecko.com/en/coins/ethereum')
eth_string = BeautifulSoup(response.data,features="lxml")  # Note the use of the .data property
eth_string=str(eth_string)
eth_string=eth_string[eth_string.find('{"@type":"Offer","price":"'):eth_string.find('","priceCurrency":"USD"}}')]
eth_string=float(eth_string[26:])
print(eth_string)
'''
