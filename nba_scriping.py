import requests
from bs4 import BeautifulSoup
import pandas as pd 
from pymongo import MongoClient


# Récupère et parse le site 
url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html#per_game_stats::pts_per_g'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# Récupère le header du tableau
#table_title = []
#thead = soup.find('thead')
#for th in thead.find_all('th'):
#    table_title.append(th.text)
#table_title.remove('Rk')
#print(table_title)

# Récupère les stats d'un joueur sur ses 5 dernières saisons et retourne un dataframe 
def scrap_player(urll):
    response = requests.get(urll, timeout=6)
    soup2 = BeautifulSoup(response.content, 'lxml')
    theads = soup2.find('thead')
    tbodys = soup2.find('tbody')
    table_head = []
    table_body = []
    for th in theads.find_all('th'):
        table_head.append(th.text)
    print(len(table_head))
    df = pd.DataFrame(columns = table_head)
    for tr in tbodys.find_all('tr', class_="full_table")[0:5]:
        tds = tr.find_all(['th', 'td'])
        row_content = [td.text for td in tds]
        length = len(df)
        df.loc[length] = row_content
        table_body.append(row_content)
    toConvert = ['G', 'GS', 'MP', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'FG%', '3P%', 'FT%', 'eFG%']
    for i in toConvert:
        df[i] = pd.to_numeric(df[i], errors = 'coerce')
    df['Season'] = df['Season'].str[0:2]+df['Season'].str[5:7]
    df['Season'] = pd.to_datetime(df['Season'], errors = 'coerce').dt.year
    return df


# Récupère l'ensemble des joueur de la saison 2021/2022 
#table_content = []
#row_content = []
links = []
tbody = soup.find('tbody')
for tr in tbody.find_all('tr', class_="full_table")[0:2]:
    #tds = tr.find_all('td')
    #row_content = [td.text for td in tds]
    #table_content.append(row_content)
    a = tr.find('a')
    link = a['href']
    links.append('https://www.basketball-reference.com/' + link)
    #print(row_content)
#print(len(table_content))
#print(len(links))

list_player = []
for urls in links[0:5]:
    player = scrap_player(urls)
    list_player.append(player)
print(list_player)
# Récupère les stats des 5 dernières saison pour chaque joueur
#last_seasons = []
#for urls in links:
#    r2 = requests.get(urls, timeout=6)
#   soup2 = BeautifulSoup(r2.content, 'lxml')
#
    #thead2 = soup2.find('thead')
    #for th in thead2.find_all('th'):
    #    last_seasons.append(th.text)
#    tbody2 = soup2.find('tbody')
#    for tr in tbody2.find_all('tr', class_="full_table")[0:5]:
 #       tds = tr.find_all('td')
  #      row_content = [td.text for td in tds]
   #     print(row_content)
    #    last_seasons.append(row_content)
#print(len(last_seasons))
    #print(row_content)
    #print(len(table_content))
    #print(len(links))
