import requests
from bs4 import BeautifulSoup
import pandas as pd 
import pymongo


def scrap_player(urll):
    """
        Récupère les stats d'un joueur sur ses 5 dernières saisons 

        params: url de la page du joueur

        return: dataframe contenant l'ensemble de ses stats sur ses 5 derniers saisons
    """
    # Récupère et parse la page
    response = requests.get(urll, timeout=20)
    soup2 = BeautifulSoup(response.content, 'lxml')
    theads = soup2.find('thead')
    tbodys = soup2.find('tbody')
    name_player = soup2.find('h1')

    # Récupère le titre du tableau et initialise le dataframe
    table_head = []
    for th in theads.find_all('th'):
        table_head.append(th.text)
    table_head.append('player')
    df = pd.DataFrame(columns = table_head)

    # Récupère le contenu du tableau (ligne de stat) et l'ajoute dans le dataframe
    for tr in tbodys.find_all('tr', class_="full_table")[-10:]:
        tds = tr.find_all(['th', 'td'])
        row_content = [td.text for td in tds]
        row_content.append(name_player.text.strip())
        length = len(df)
        df.loc[length] = row_content

    # Convertit certaine colonne du datframe en numeric
    toNumeric = ['G', 'GS', 'MP', 'FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'FG%', '3P%', '2P%','FT%', 'eFG%']
    for i in toNumeric:
        df[i] = pd.to_numeric(df[i], errors = 'coerce')
    # Convertit la date
    df['Season'] = df['Season'].str[0:2]+df['Season'].str[5:7]
    df['Season'] = pd.to_datetime(df['Season'], errors = 'coerce').dt.year

    return df

def main():

    # Récupère et parse la page
    url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html#per_game_stats::pts_per_g'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    # Connexion avec Mongodb
    client = pymongo.MongoClient('nba_mongo:27017')
    database = client['NBA']
    collection = database['Player']
    collection.delete_many({}) # suppression des éléments déjà présent


    # Récupère l'ensemble des liens allant sur la page de stats de chaque joueur
    links = []
    tbody = soup.find('tbody')
    for tr in tbody.find_all('tr', class_="full_table"):
        a = tr.find('a')
        link = a['href']
        links.append('https://www.basketball-reference.com/' + link)

    # Récupère dataframes pour tous les joueurs de la listes et les ajoutes dans la collection
    list_player = []
    for urls in links:
        player = scrap_player(urls)
        list_player.append(player)
        dic_player = player.to_dict(orient='records')
        collection.insert_many(dic_player)
        



if __name__ == '__main__':
    main()
