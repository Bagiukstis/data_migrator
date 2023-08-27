from import_decorator import procedure
import logging

logging = logging.getLogger(__name__)


@procedure("CheckDates")
def checkdates(df, table_name):
    """
    Checks if the dates that are present in the table are following the correct order.

    :param df: DataFrame
    :param table_name: table_name
    :return: bool -> True if incorrect
    """
    date_columns = ["order_date", "required_date", "shipped_date"]
    if any(col in df.columns for col in date_columns):
        order_date = (
            df[date_columns]["order_date"] <= df[date_columns]["required_date"]
        ).all()
        if order_date == False:
            msg = f"Dataframe with table name: {table_name} has wrongly formatted dates"
            logging.warning(msg)
            print(msg)
            return True

    return False
