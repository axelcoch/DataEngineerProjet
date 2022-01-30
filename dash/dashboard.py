import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_table
from dash import callback_context
import dash_bootstrap_components as dbc
import pymongo
import plotly.express as px
import pandas as pd

# Connexion avec Mongodb
client = pymongo.MongoClient('nba_mongo:27017')
database = client['NBA']
collection = database['Player']

def generate_page():
    # Création de df pour l'affichage des données
    data1 = pd.DataFrame(list(collection.find({"PTS":{'$gt':26.00}})))[["Season", "PTS", "player"]]
    data2 = pd.DataFrame(list(collection.find({"AST":{'$gt':8.00}})))[["Season", "AST","player"]]
    data3 = pd.DataFrame(list(collection.find({})))[["Season", "Tm", "PTS"]]
    data4 = pd.DataFrame(list(collection.find({})))[["Season", "Tm", "AST"]]
    data5 = pd.DataFrame(list(collection.find({"TOV":{'$gt':2.80}})))[["Season", "Tm", "TOV"]]
    data6 = pd.DataFrame(list(collection.find({"TOV":{'$gt':3.50}})))[["Season", "player", "TOV"]]


    # Création de graphique pour l'affichage des données
    bar1 = px.bar(data1, x = "player", y = "PTS", barmode="group", facet_col="Season") 
    bar2 = px.bar(data2, x = "player", y = "AST", barmode="group", facet_col="Season") 
    bar3 = px.bar(data3, x = "Tm", y = "PTS", barmode="group", facet_col="Season")
    bar4 = px.bar(data4, x = "Tm", y = "AST", barmode="group", facet_col="Season")
    funnel = px.funnel(data5, x = "TOV", y="Tm")
    funnel2 = px.funnel(data6, x = "TOV", y="player")

    return html.Div(style={'font-family' : 'Trebuchet MS, sans-serif'}, children=[
        html.Div( id="header", children=[
            html.H2(id = "titre", children=f'NBA Scraping',
                            style={'textAlign': 'center', 'color': '#FFFFFF', 'fontSize': 60}),
            
            html.H4(id = "name", children=f'Romain Bourdeaux - Axel Cochet', 
                            style={'textAlign': 'center', 'color': '#FFFFFF', 'marginBottom': '75px'}),

            html.H3(id = "Description", 
                        children=f'Ce projet permet de récupérer les statistiques des 5 dernières saisons des 590 joueurs de la saisons 2021-2022 à partir du site basketball reference.',
                        style={'textAlign': 'center', 'color': '#FFFFFF', 'marginBottom': "100px"}),
        ]),

        dcc.Tabs([
            dcc.Tab(label='Statistiques générales', children=[
                html.Div(children=[
                #html.Button('Refresh', id='Refresh', n_clicks=0),
                html.H5('Joueurs ayant marqués plus de 26 pts par saison', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px'},
                    id = 'graph1',
                    figure = bar1
                ),
                html.H5('Joueurs ayant effectués plus de 7 ast par saison', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph2',
                    figure = bar2
                ),
                html.H5('Equipe ayant effectués marqué le plus de pts par saison', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph3',
                    figure = bar3
                ),
                html.H5('Equipe ayant effectués le plus de ast par saison', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph4',
                    figure = bar4
                ),
                html.H5('Nombre de perte de balle par équipe', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph5',
                    figure = funnel
                ),
                html.H5('Nombre de perte de balle par joueur', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph6',
                    figure = funnel2
                ),
                ]),
            ], style={'fontSize': 20, 'color' : 'black'}),
        ]),    
    ]
    )




if __name__ == '__main__':

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY]) 

    app.layout = generate_page # démarrer la page

    #
    # RUN APP
    #

    app.run_server(debug=True, host = '0.0.0.0') # (8)