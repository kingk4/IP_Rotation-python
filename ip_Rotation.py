import requests
from itertools import cycle
import traceback
from lxml.html import fromstring
def proproxies():
    def get_proxies():                                                                                     # Proxies sites !!!
        url = 'https://free-proxy-list.net/'                                         # https://www.sslproxies.org/    &&   https://free-proxy-list.net/ !!!    
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[1:5]:                                    # take proxies from site !!!
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                #Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies
    proxies = get_proxies()
    print(proxies)
    length_proxies =len(proxies)
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    url = 'https://httpbin.org/ip'
    for i in range(length_proxies):
        proxy = next(proxy_pool)
        #print(proxy)
        # print("Request #%d"%i)
        try:
            response = requests.get(url, proxies={"http": proxy, "http_1": proxy}, timeout=3)                      # Rotataing proxies  !!!
            print(response.json())
        except:
            print("Skipping. Connnection error")
proproxies()

