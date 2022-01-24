import requests
from bs4 import BeautifulSoup
import pandas as pd 

# Récupère et parse le site 
url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html#per_game_stats::pts_per_g'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# Récupère le header du tableau
table_title = []
thead = soup.find('thead')
for th in thead.find_all('th'):
    table_title.append(th.text)
table_title.remove('Rk')
print(table_title)

# Récupère l'ensemble des stats de la saison 2021/2022 pour chaque joueur
table_content = []
row_content = []
links = []
tbody = soup.find('tbody')
for tr in tbody.find_all('tr', class_="full_table"):
    tds = tr.find_all('td')
    row_content = [td.text for td in tds]
    table_content.append(row_content)
    a = tr.find('a')
    link = a['href']
    links.append('https://www.basketball-reference.com/' + link)
    #print(row_content)
print(len(table_content))
print(len(links))


# Récupère les stats des 5 dernières saison pour chaque joueur
last_seasons = []
for urls in links:
    r2 = requests.get(urls, timeout=6)
    soup2 = BeautifulSoup(r2.content, 'lxml')

    thead2 = soup2.find('thead')
    for th in thead2.find_all('th'):
        last_seasons.append(th.text)
    tbody2 = soup2.find('tbody')
    for tr in tbody2.find_all('tr', class_="full_table"):
        tds = tr.find_all('td')
        row_content = [td.text for td in tds]
        last_seasons.append(row_content)
print(len(last_seasons))
    #print(row_content)
    #print(len(table_content))
    #print(len(links))
