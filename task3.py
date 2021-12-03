#Делаем 1000 Get запросов к сайту и отображаем прогресс-бар
# Не делал никаких доп проверок, так как не было этого в условии :-)

import requests
from tqdm import tqdm

def site_res(url_site):
    for i in tqdm(range(100)):
        res = requests.get(url_site)       
        #print(res)

url_site = input('Введите адрес сайта')
site_res(site)
