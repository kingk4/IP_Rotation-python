import time
import requests
from fp.fp import FreeProxy                               

for i in range(4):
    try:
        proxies = FreeProxy(rand=True).get()
        #proxies = FreeProxy(country_id=['US', 'CA', 'FR', 'JP', 'BR', 'DE' ], rand=True).get()
        print(proxies)
        proxy={
            'http': proxies,
            'https': proxies
        }
        location = requests.get('https://httpbin.org/ip', proxies=proxy)
        print(location.json())
        time.sleep(1)
    except:
        pass