from import_decorator import procedure
import logging

logging = logging.getLogger(__name__)


@procedure("CheckPrices")
def checkprices(df, table_name):
    """
    Checks for negative prices in the "list_price" column

    :param df: DataFrame
    :param table_name: table_name
    :return: bool -> True if contains negative prices
    """
    if not "list_price" in df.columns:
        return False

    list_price = df[df["list_price"] < 0].any().any()
    if list_price:
        msg = f"Dataframe with table name: {table_name} in column list_price contains negative prices"
        print(msg)
        logging.warning(msg)
        return True

    return False
