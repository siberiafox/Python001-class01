import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import numpy as np

# pretend as web client
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['User-Agent'] = user_agent
header['Cookie'] = '__mta=141999757.1593174899684.1593176618684.1593182040854.17; uuid_n_v=v1; uuid=76A3BE20B7A911EAAD7CEBC74F78E0F9447DA73DC8AD402493E9A96F45D4AF97; _csrf=39451b8b9279c90e9b8922e76cb691b101a61c1c1d86af9b7da7f8f19a21f9ba; _lxsdk_cuid=172f09fbbc4c8-01eb39c9dae05d-4e4c0f20-1fa400-172f09fbbc4c8; _lxsdk=76A3BE20B7A911EAAD7CEBC74F78E0F9447DA73DC8AD402493E9A96F45D4AF97; mojo-uuid=1e55f39ae2fa273dfbf4991a578c003d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593174900,1593176675; mojo-session-id={"id":"dd4f1a0e2be9d2ed4985156569b30a2d","time":1593190983185}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593190983; __mta=141999757.1593174899684.1593182040854.1593190983279.18; _lxsdk_s=172f19141f6-44b-1c6-83f%7C%7C4'

# target url address
url_maoyan = 'https://maoyan.com/films?showType=3'

# get method and return a response obj instance
respo = requests.get(url=url_maoyan,headers=header)

if respo.status_code == 200:
    print('get the respo construction!')
    #bs sparse the respo's text part
    beaut = bs(respo.text, 'html.parser')
    col_names = ['film_name','film_score','film_type','film_actors','film_rel_date']
    l = []
    print(len(beaut.find_all('dd')),len(beaut.find_all('div', attrs={'class':re.compile(r'movie-hover-title(\s\w+)?')})))
    for idx,div in enumerate(beaut.find_all('div', attrs={'class':re.compile(r'movie-hover-title(\s\w+)?')})):
        spans = div.find_all('span')
        if idx % 4 == 0:
            if len(spans) > 1:
                l.append(spans[0].text)
                iss = spans[1].find_all('i')
                l.append(iss[0].text + iss[1].text)
            else:
                l.append(spans[0].text)
                l.append(None)
        else:
            info = div.get_text().split()
            if len(info)>1:
                l.append(info[1].strip())
            else:
                l.append(info[0].strip())
    print(l,len(l))
    df = pd.DataFrame(np.array(l).reshape(30,5),columns=col_names)
    print('saving file to loc ...')
    df.to_csv('./PAC3/week01/job1_result.csv',encoding='utf8',index=False)
    print('saved in current path')
else:
    print('there are something wrong, checkout later!')









