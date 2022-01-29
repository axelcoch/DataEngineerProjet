import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import callback_context
import dash_bootstrap_components as dbc
import pymongo

if __name__ == '__main__':

    # Connexion avec Mongodb
    client = pymongo.MongoClient('nba_mongo:27017')
    database = client['NBA']

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY]) 

    app.layout = html.Div(style={'font-family' : 'Trebuchet MS, sans-serif'}, children=[
        html.Div( id="header", children=[
            html.H2(id = "titre", children=f'NBA Scraping',
                            style={'textAlign': 'center', 'color': '#FFFFFF', 'fontSize': 60}),
            
            html.H4(id = "name", children=f'Romain Bourdeaux - Axel Cochet', 
                            style={'textAlign': 'center', 'color': '#FFFFFF', 'marginBottom': '75px'}),

            html.H3(id = "Description", 
                        children=f'Ce projet permet de récupérer les statistiques des 5 dernières saisons des 590 joueurs de la saisons 2021-2022 à partir du site basketball reference.',
                        style={'textAlign': 'center', 'color': '#FFFFFF', 'marginBottom': "100px"}),
        ]),

        #Création du menu déroulant pour le choix des années
        html.Div(children=[
            html.Label('Choix du joueur', style={'textAlign': 'center', 'marginBottom': '20px'}),
            dcc.Dropdown(
                id="player_option",
                options = [
                {'label': '2016', 'value': 2016},
                {'label': '2017', 'value': 2017},
                {'label': '2018', 'value': 2018}
                ],

                style={"textAlign" : "center", "fontSize": "20px", "color": "black"}
            ),
        ], style={'width': '60%', 'margin': 'auto'}),
    ]
    )

    

    #
    # RUN APP
    #

    app.run_server(debug=True, host = '0.0.0.0') # (8)