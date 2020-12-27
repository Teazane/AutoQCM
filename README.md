# AutoQCM
Projet de génération aléatoire de QCM à partir d'une BDD de questions.

## Présentation et objectif
Le but du projet est de proposer un outil pour automatiser la création et la correction de QCM.
L'outil s'appuie sur une base de données constituée de questions associées à leurs réponses (bonnes ou mauvaises) et leurs caractéristiques (difficulté, durée de résolution, niveau scolaire, ...).
L'outil doit proposer une interface afin de paramétrer un questionnaire qui sera généré et pourra être soumis au logiciel AMC (https://www.auto-multiple-choice.net/index.fr).

## Initialiser le projet
- Installer Python 3 : https://www.python.org/downloads/
- Installer Git : https://git-scm.com/downloads 
- Récupérer le code en clonant le dossier : `git clone https://github.com/Teazane/AutoQCM.git`
- (optionnel) Installer virtualenv avec la commande : `pip install virtualenv`
- (optionnel) Créer l'environnement virtuel : `virtualenv env`
- (optionnel) Activer l'environnement virtuel : `.\env\Scripts\activate`
- Installer les dépendances du projet : `pip install -r requirements.txt`
- Initialiser la variable FLASK_APP (sous Cmd : `set FLASK_APP=App.py`, sous PS : `$env:FLASK_APP="App.py"`, sous Linux : `export FLASK_APP=App.py`)

Il ne reste plus qu'à lancer le projet avec `flask run`.

Pour mettre à jour le projet, lancer `git pull`.

## Organisation du code
- App.py : permet de lancer l'appli' Flask
- app_src : contient les fichiers nécessaires à l'appli' Flask
    - config.py : contient les variables de configuration de l'appli' Flask
    - routes.py : contient les routes de l'appli' Flask
    - templates : dossier contenant les templates HTML à afficher
- data_management : contient les fichiers nécessaires à l'utilisation de la BDD
    - data_loader.py : contient les classes nécessaires à la lecture de la BDD

## Erreurs connues
### Erreur de Numpy lors du chargement des données Excel
Reproduction de l'erreur :
```
> python data_loader.py
 ** On entry to DGEBAL parameter number  3 had an illegal value
 ** On entry to DGEHRD  parameter number  2 had an illegal value
 ** On entry to DORGHR DORGQR parameter number  2 had an illegal value
 ** On entry to DHSEQR parameter number  4 had an illegal value
Traceback (most recent call last):
  File "data_loader.py", line 1, in <module>
    from pandas import read_excel, read_csv
  File "C:\...\AutoQCM\env\lib\site-packages\pandas\__init__.py", line 11, in <module>
    __import__(dependency)
  File "D:\...\AutoQCM\env\lib\site-packages\numpy\__init__.py", line 305, in <module>
    _win_os_check()
  File "D:\...\AutoQCM\env\lib\site-packages\numpy\__init__.py", line 302, in _win_os_check
    raise RuntimeError(msg.format(__file__)) from None
RuntimeError: The current Numpy installation ('D:\\...\\AutoQCM\\env\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3dm3h86
```
Résolution de l'erreur :

La version de Numpy incluse dans la bibliothèque Pandas cause une erreur.
Il faut donc en changer la version de 1.19.4 à 1.19.3 :
```
> pip install --upgrade numpy==1.19.3
```

## Built with / using
- Python (3.6) - see used libs in `requirements.txt`
- Excel from Microsoft Office
- AMC - https://www.auto-multiple-choice.net/index.fr

## Auteur et license
Codé avec amour par Teazane.
Licence MIT.