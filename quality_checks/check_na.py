from import_decorator import procedure
import logging

logging = logging.getLogger(__name__)


@procedure("CheckNA")
def checkna(df, table_name):
    """
    Checks if the data contains NaN values in any column

    :param df: DataFrame
    :param table_name: table_name
    :return: bool -> True if contains NaN values
    """
    if df.isna().any().any():
        # Lets find what columns contain NA vals
        col_idx = df.columns[df.isna().any() == True]
        for col_name in col_idx:
            msg = f"Dataframe with table name: {table_name} in column: {col_name} contains NaN values"
            print(msg)
            logging.warning(msg)

            # Can also provide additional information where exactly we have NaN's if requested.
            # na_length = len(df[df[col_name].isnull()])
            # report_dct[col_name] = na_length
        return True
    return False
