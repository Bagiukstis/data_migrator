from import_decorator import procedure
import logging

logging = logging.getLogger(__name__)


@procedure("CheckDupes")
def checkdupes(df, table_name):
    """
    Checks for duplicate rows in the data

    :param df: DataFrame
    :param table_name: table_name
    :return: bool -> True if contains duplicates
    """

    if df.duplicated().any():
        msg = f"Dataframe with table name: {table_name} contains duplicate values"
        print(msg)
        logging.warning(msg)
        return True
    return False
