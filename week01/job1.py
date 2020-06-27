import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

# pretend as web client
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['User-Agent'] = user_agent
header['Cookie'] = '__mta=141999757.1593174899684.1593182040854.1593223784235.18; uuid_n_v=v1; uuid=76A3BE20B7A911EAAD7CEBC74F78E0F9447DA73DC8AD402493E9A96F45D4AF97; _lxsdk_cuid=172f09fbbc4c8-01eb39c9dae05d-4e4c0f20-1fa400-172f09fbbc4c8; _lxsdk=76A3BE20B7A911EAAD7CEBC74F78E0F9447DA73DC8AD402493E9A96F45D4AF97; mojo-uuid=1e55f39ae2fa273dfbf4991a578c003d; _csrf=840b6bc96695ecc3bbf1b0c103440e72fff6e0b19480bd2f5c97434956ac2caa; mojo-session-id={"id":"4c0e0ce4bec27a2470db6f8c48856c37","time":1593223742872}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593174900,1593176675,1593223743,1593224927; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593224927; __mta=141999757.1593174899684.1593223784235.1593224927483.19; mojo-trace-id=11; _lxsdk_s=172f3890592-196-8ff-733%7C%7C29'

# target url address
url_maoyan = 'https://maoyan.com/films?showType=3'

# get method and return a response obj instance
respo = requests.get(url=url_maoyan,headers=header)
print('text of respo is: ',respo.text)

if respo.status_code == 200:
    print('get the respo construction!')
    #bs sparse the respo's text part
    beaut = bs(respo.text, 'html.parser')
    col_names = ['film_name','film_score','film_type','film_actors','film_rel_date']
    ary = []

    divs= beaut.find_all('div', attrs={'class':re.compile(r'movie-hover-title.*')})

    assert len(divs) > 0, 'the resqust may be shield!'

    for idx,div in enumerate(divs):
        spans = div.find_all('span')
        if idx % 4 == 0:
            if len(spans) > 1:
                ary.append(spans[0].text)
                iss = spans[1].find_all('i')
                ary.append(iss[0].text + iss[1].text)
            else:
                ary.append(spans[0].text)
                ary.append(None)
        else:
            info = div.get_text().split()
            if len(info)>1:
                ary.append(info[1].strip())
            else:
                ary.append(None)
    df = pd.DataFrame(np.array(ary).reshape(-1,len(col_names)),columns=col_names)
    print('saving file to loc ...')
    df.to_csv('./PAC3/week01/job1_result.csv',encoding='utf8',index=False)
    print('saved in current path')
else:
    print('there are something wrong, checkout later!')









