# **DataEngineeringProjet : nba scrapping**

## **Description**

Ce projet permet de récupérer les statistiques des 5 dernières saisons des 590 joueurs de la saisons 2021-2022 à partir du site [basketball reference](https://www.basketball-reference.com).

Ce projet est réalisé dans le cadre scolaire. Le but est d'avant tout d'apprendre à scraper des données avec plusieurs outils simples. Nous avons également réalisé un dashboard afin d'afficher les données récupérées.  

<br>

## **User Guide**

### **Récupération du projet**

Tout d'abord verifiez que vous avez bien installé [Git](https://git-scm.com/) sur votre espace de travail afin de récupérer les fichiers.
Ensuite, clonez le dossier dans le répertoire souhaité en utilisant la commande [git clone](https://github.com/axelcoch/DataEngineerProjet.git) afin d'avoir accès au répertoire.

```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > git clone https://github.com/axelcoch/DataEngineerProjet.git
$:~/<WORKDIR> > cd DataEngineerProjet/
$:~/<WORKDIR> > ls
dash  docker-compose.yml  scrap  README.md 
```

<br>

### **Lancement du projet**

Avant de faire les manipulations suivantes, il faut s'assurer que [docker](https://docs.docker.com/get-docker/) soit bien installé. 
Ensuite, mettez vous dans le bon répertoire et lancez la commande `docker-compose up`. Cette commande va lancer l'environnement.
```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > cd DataEngineerProjet/
$:~/<WORKDIR> > docker-compose up
```

> Pour lancer le dashboard, il faut se rendre à l'adresse suivante `http://localhost:8050/`. 

<br>

### **Fonctionnement du dashboard**

Le Dashbaord est ainsi composé d'un onglet `Statistiques générales` contenant certains graphiques utiles pour l'affichage des données. Ne pas hésiter à zoomer sur les joueurs.

<br>

### **Composition du projet et liste des technologies utilisés**

Le projet est composé de 2 fichiers python :
* *nba_sciping.py* afin de récupérer les données et de les pousser dans notre base de données.
* *dashboard.py* afin d'afficher les données dans un dashboard intéractif.

Pour le scraping de données, nous avons utilisé :
* *requests* afin de faire nos requetes html (requêtes GET).
* *beautifulsoup* (bs4) afin de parser le code que l'on a récupéré.

Pour le traîtement et le stockage des données :
* *pandas* pour stocker nos données dans un dataframe afin de les traiter un peu.
* *mongodb* afin de stocker nos données transformées dedans pour les réutiliser plus tard.
  
Pour l'affichage des données :
* *Dash* afin de créer un dashboard intéractif.
* *Plotly express* afin de faire de mettre les données sous forme de graphique.

 
<br>

*<div style="text-align: right"> Axel Cochet - Romain Bourdeaux</div>*



*********
********
********
<br>

####  *English version*

<br>

## **Description**

This project allows us to recover the statistics from the last 5 seasons of the 590 players that are currently playing in the 2021-2022 season, all from the website [basketball reference](https://www.basketball-reference.com).

This project is a school project. Our goal is mainly to be able to scrap data with several easy tools. The recovered data is displayed in a dashboard.  

<br>

## **User Guide**

### **Recovery of the project**

First of all make sure you installed [Git](https://git-scm.com/) correctly on your workspace, in order to get all the files.
Then, clone the file in the chosen directory using the [git clone](https://github.com/axelcoch/DataEngineerProjet.git) command in order to access the directory.

```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > git clone https://github.com/axelcoch/DataEngineerProjet.git
$:~/<WORKDIR> > cd DataEngineerProjet/
$:~/<WORKDIR> > ls
dash  docker-compose.yml  scrap  README.md 
```

<br>

### **Launching the project**

Before executing the following comamnds, make sure that [docker](https://docs.docker.com/get-docker/) is well installed. 
Then, select the right directory and execute the `docker-compose up` command. Ths will launch the whole environnement.
```
$:~/> cd <WORKDIR>
$:~/<WORKDIR> > cd DataEngineerProjet/
$:~/<WORKDIR> > docker-compose up
```

> To launch the dashboard, click on the following link: `http://localhost:8050/`. 

<br>

### **Operating the dashboard**

The Dashbaord is made of a tab `Statistiques Générales` that contains some useful graphs to display the data. Don't mind to zoom on the players.

<br>

### **Composition of the project and list of the used technologies**

The project is made of two Python files:
* *nba_sciping.py* to recover data and push it into our database.
* *dashboard.py* to display data in an interactive dashboard.

To scrap the data, we used:
* *requests* for the html requests (GET requests).
* *beautifulsoup* (bs4) to parse the code we just got.

To treat and store data:
* *pandas* to store data in a dataframe, in order to treat them a bit.
* *mongodb* to store the transformed data in order to use it later.
  
To display data:
* *Dash* to create an interactive dashboard.
* *Plotly express* to display the data in graphs.

<br>

*<div style="text-align: right"> Axel Cochet - Romain Bourdeaux</div>*