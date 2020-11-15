# AutoQCM
Projet de génération aléatoire de QCM à partir d'une BDD de questions.

## Présentation et objectif
Le but du projet est de proposer un outil pour automatiser la création et la correction de QCM.
L'outil s'appuie sur une base de données constituée de questions associées à leurs réponses (bonnes ou mauvaises) et leurs caractéristiques (difficulté, durée de résolution, niveau scolaire, ...).
L'outil doit proposer une interface afin de paramétrer un questionnaire qui sera généré et pourra être soumis au logiciel AMC (https://www.auto-multiple-choice.net/index.fr).

## Initialiser le projet
- Installer Python 3
- (optionnel) Installer virtualenv avec la commande : `pip install virtualenv`
- (optionnel) Créer l'environnement virtuel : `virtualenv env`
- (optionnel) Activer l'environnement virtuel : `.\env\Scripts\activate`
- Installer les dépendances du projet : `pip install -r requirements.txt`
- Initialiser la variable FLASK_APP (sous Cmd : `set FLASK_APP=App.py`, sous PS : `$env:FLASK_APP="App.py"`, sous Linux : `export FLASK_APP=App.py`)

Il ne reste plus qu'à lancer le projet avec `flask run`.

## Built with / using
- Python (3.6) - see used libs in `requirements.txt`
- Excel from Microsoft Office
- AMC - https://www.auto-multiple-choice.net/index.fr

## Auteur et license
Codé avec amour par Teazane.
Licence MIT.