import os

class Config(object):
    """
        Classe Config permettant de définir toutes les variables de configuration
        nécessaire à l'application Flask.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # TODO: A changer quand lancement en prod'