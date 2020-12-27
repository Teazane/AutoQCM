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

class CorrespondingTablesLoader:
    """
        Classe CorrespondingTablesLoader permettant de charger les tables de correspondance 
        de la BDD depuis un fichier Excel ou CSV au besoin.
    """

    def __init__(self, bdd_file_path):
        """
            Constructeur de la classe CorrespondingTablesLoader.
            Initialise le logger et charge les données du fichier passé en paramètre.

            :param bdd_file_path: Chemin du fichier xlsx à lire.
            :type bdd_file_path: string
        """
        logging.basicConfig(format='%(asctime)s %(levelname)s [%(module)s (%(funcName)s)] %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG)
        logging.info("Data base file reading...")
        self.dataframe_level_from_xlsx = read_excel(bdd_file_path, sheet_name="Num-Niveau")
        self.dataframe_difficulty_from_xlsx = read_excel(bdd_file_path, sheet_name="Num-Difficulté")
        self.dataframe_notion_from_xlsx = read_excel(bdd_file_path, sheet_name="Num-Rudiment")
        self.dataframe_subject_from_xlsx = read_excel(bdd_file_path, sheet_name="Num-Discipline")

    def get_corresponding_level(self, level):
        """
            Méthode pour trouver le nom d'un niveau scolaire à partir de son ID.

            :param level: ID du niveau scolaire cherché.
            :type level: int
            :return: Nom du niveau scolaire. 
            :rtype: string
        """
        res = self.dataframe_level_from_xlsx["Niveau"][self.dataframe_level_from_xlsx["Num-Niveau"] == level]
        return res.iloc[0]

    def get_corresponding_difficulty(self, difficulty):
        """
            Méthode pour trouver le nom d'un niveau de difficulté à partir de son ID.

            :param difficulty: ID du niveau de difficulté cherché.
            :type difficulty: int
            :return: Nom du niveau de difficulté. 
            :rtype: string
        """
        res = self.dataframe_difficulty_from_xlsx["Difficulté"][self.dataframe_difficulty_from_xlsx["Num-Difficulté"] == difficulty]
        return res.iloc[0]

    def get_corresponding_notion(self, notion):
        """
            Méthode pour trouver le nom d'une notion à partir de son ID.

            :param notion: ID d'une notion cherché.
            :type notion: int
            :return: Nom d'une notion. 
            :rtype: string
        """
        res = self.dataframe_notion_from_xlsx["Rudiment"][self.dataframe_notion_from_xlsx["Num-Rudiment"] == notion]
        return res.iloc[0]

    def get_corresponding_subject(self, subject):
        """
            Méthode pour trouver le nom d'une matière scolaire à partir de son ID.

            :param subject: ID d'une matière scolaire cherchée.
            :type subject: int
            :return: Nom d'une matière scolaire. 
            :rtype: string
        """
        res = self.dataframe_subject_from_xlsx["Discipline"][self.dataframe_subject_from_xlsx["Num-Discipline"] == subject]
        return res.iloc[0]

if __name__ == '__main__':
    # Main used for test
    ql = QuestionLoader("BDD-Questions.xlsx")
    print(ql.get_all_questions_with_filter(level=9))
    print(ql.get_all_questions_with_filter(level=9, difficulty=4))
    ctl = CorrespondingTablesLoader("BDD-Questions.xlsx")
    print(ctl.get_corresponding_level(7))
    print(ctl.get_corresponding_notion(1))