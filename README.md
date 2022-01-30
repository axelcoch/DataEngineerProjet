# DataEngineerProjet : nba scrapping

## Description

Ce projet permet de récupérer les statistiques des 5 dernières saisons des 590 joueurs de la saisons 2021-2022 à partir du site [basketball reference](https://www.basketball-reference.com).

Ce projet est réalisé dans le cadre scolaire. Le but est d'avant tout d'apprendre à scraper des données avec plusieurs outils simples. Nous avons également réalisé un dashboard afin d'afficher les données récupérées.  

## User Guide

### Récupération du projet

Tout d'abord verifiez que vous avez bien installé [Git](https://git-scm.com/) sur votre espace de travail afin de récupérer les fichiers.
Ensuite clonez le dossier dans le répertoire souhaité en utilisant la commande `git clone` https://github.com/axelcoch/DataEngineerProjet.git afin d'avoir accès au répertoire.

```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > git clone https://github.com/axelcoch/DataEngineerProjet.git
$:~/<WORKDIR> > cd DataEngineerProjet/
$:~/<WORKDIR> > ls
dash  docker-compose.yml  scrap  README.md 
```

### Lancement du projet

Avant de faire les manipulations suivantes, il faut s'assurer que [docker](https://docs.docker.com/get-docker/) soit bien installé. 
Ensuite mettez vous dans le bon répertoire et lancé la commande `docker-compose up`. Cette commande vas lancer l'environnement.
```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > cd DataEngineerProjet/
$:~/<WORKDIR> > docker-compose up
```
> Pour lancer le dashboard, il faut se rendre à l'adresse suivante `http://localhost:8050/`. 

### Fonctionnement du dashboard

Le Dashbaord est ainsi composé de deux parties, le premier onglet `Statistiques générales` contient certains graphiques utiles pour l'affichage des données et le deuxième onglet `statistiques joueurs` contient les lignes de stats du joueur choisie.

### Compositions du projet et listes des technologies utilisés.

Le projet est composé de 2 fichiers python :
* nba_sciping.py afin de récupérer les données et de les pousser dans notre base de données.
* dashboard.py afin d'afficher les données dans un dashboard intéractif.

Pour le scraping de données, nous avons utilisé :
* requests afin de faire nos requetes html ( requetes GET).
* beautifulsoup (bs4) afin de parser le code que l'on a récupéré.

Pour le traîtement et le stockage des données :
* pandas pour stockés nos données dans un dataframe afin de les traîter un peu.
* mongodb afin de stockés nos données transformées dedans pour les réutiliser plus tard.
  
Pour l'affichage des données :
* Dash afin de créer un dashboard intéractif.
* Plotly express afin de faire de mettres les données sous forme de graphique.
  
  