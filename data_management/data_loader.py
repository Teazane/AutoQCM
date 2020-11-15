from pandas import read_excel, read_csv
import logging

class DataLoader:
    """
        Classe DataLoader permettant de charger les données depuis un fichier Excel
        ou CSV au besoin.
    """

    def __init__(self, bdd_file_path):
        """
            Constructeur de la classe DataLoader.
            Initialise le logger et charge les données du fichier passé en paramètre.

            :param bdd_file_path: Chemin du fichier xlsx à lire.
            :type bdd_file_path: string
        """
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m:%d %H:%M:%S', level=logging.DEBUG)
        logging.debug("Lecture du fichier de BDD")
        self.data_in_xlsx = read_excel(bdd_file_path, sheet_name="Questions")

    def get_all_questions_for_level(self, level, subset=None):
        """
            Méthode pour sélectionner toutes les questions pour un niveau scolaire donné.

            :param level: Niveau scolaire donné.
            :param subset: (default=None) Sous-ensemble de questions éventuel.
            :type level: int
            :type subset: 
            :return: Ensemble de questions filtrées. 
            :rtype:
        """
        pass

    def get_all_questions_for_difficulty(self, difficulty, subset=None):
        """
            Méthode pour sélectionner toutes les questions pour un niveau de difficulté donné.

            :param difficulty: Niveau scolaire donné.
            :param subset: (default=None) Sous-ensemble de questions éventuel.
            :type difficulty: int
            :type subset: 
            :return: Ensemble de questions filtrées. 
            :rtype:
        """
        pass

    def get_all_questions_for_notion(self, notion, subset=None):
        """
            Méthode pour sélectionner toutes les questions pour une notion donnée.

            :param notion: Niveau scolaire donné.
            :param subset: (default=None) Sous-ensemble de questions éventuel.
            :type notion: int
            :type subset: 
            :return: Ensemble de questions filtrées. 
            :rtype:
        """
        pass

    def get_all_questions_for_subject(self, subject, subset=None):
        """
            Méthode pour sélectionner toutes les questions pour une matière scolaire donnée.

            :param subject: Niveau scolaire donné.
            :param subset: (default=None) Sous-ensemble de questions éventuel.
            :type subject: int
            :type subset: 
            :return: Ensemble de questions filtrées. 
            :rtype:
        """
        pass

if __name__ == '__main__':
    dl = DataLoader("BDD-Questions.xlsx")