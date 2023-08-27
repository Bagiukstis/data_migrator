from import_decorator import procedure
import re
import logging

logging = logging.getLogger(__name__)


@procedure("CheckEmail")
def checkemail(df, table_name):
    """
    Checks if the email pattern is correct in the email column

    :param df: DataFrame
    :param table_name: table_name
    :return: bool -> True if incorrect
    """

    def _is_valid_email(email):
        email_pattern = r"^[a-zA-Z0-9._%'+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        match = re.match(email_pattern, email)
        return bool(match) if match else False

    if "email" in df.columns:
        email_validity = df["email"].apply(_is_valid_email)
        if email_validity.all() == False:
            msg = f"Dataframe with table name: {table_name} contains invalid emails"
            print(msg)
            logging.warning(msg)
            return True

    return False
