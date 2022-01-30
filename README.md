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


  