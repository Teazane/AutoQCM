from pandas import read_excel, read_csv
import logging

class QuestionLoader:
    """
        Classe QuestionLoader permettant de charger la BDD de questions depuis un fichier 
        Excel ou CSV au besoin.
    """

    def __init__(self, bdd_file_path):
        """
            Constructeur de la classe QuestionLoader.
            Initialise le logger et charge les données du fichier passé en paramètre.

            :param bdd_file_path: Chemin du fichier xlsx à lire.
            :type bdd_file_path: string
        """
        logging.basicConfig(format='%(asctime)s %(levelname)s [%(module)s (%(funcName)s)] %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG)
        logging.info("Data base file reading...")
        self.dataframe_from_xlsx = read_excel(bdd_file_path, sheet_name="Questions")
        logging.debug("File content:\n" + str(self.dataframe_from_xlsx))

    def get_all_questions_with_filter(self, level=None, difficulty=None, notion=None, subject=None, subset=None):
        """
            Méthode pour sélectionner toutes les questions selon un ensemble de filtres donnés.
            Ces filtres peuvent être : le niveau scolaire, la difficulté, la notion abordée, ou
            la matière scolaire concernée.

            :param level: ID du niveau scolaire donné.
            :param difficulty: ID du niveau de difficulté donné.
            :param notion: ID de la notion donnée.
            :param subject: ID de la matière scolaire donnée.
            :param subset: (default=None) Sous-ensemble de questions éventuel.
            :type level: int
            :type difficulty: int
            :type notion: int
            :type subject: int
            :type subset: pandas.DataFrame
            :return: Ensemble de questions filtrées. 
            :rtype: pandas.DataFrame
        """
        if subset is not None:
            data_to_filter = subset
        else:
            data_to_filter = self.dataframe_from_xlsx
        # Ici on filtre le data frame avec chaque filtre renseigné, l'un après l'autre
        if level is not None:
            data_to_filter = data_to_filter[data_to_filter["Num-Niveau"] == level]
        if difficulty is not None:
            data_to_filter = data_to_filter[data_to_filter["Num-Difficulté"] == difficulty]
        if notion is not None:
            data_to_filter = data_to_filter[data_to_filter["Num-Rudiment"] == notion]
        if subject is not None:
            data_to_filter = data_to_filter[data_to_filter["Num-Discipline"] == subject]
        return data_to_filter
        

if __name__ == '__main__':
    # Main used for test
    ql = QuestionLoader("BDD-Questions.xlsx")
    print(ql.get_all_questions_with_filter(level=9))
    print(ql.get_all_questions_with_filter(level=9, difficulty=4))