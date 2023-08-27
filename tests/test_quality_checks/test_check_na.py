import unittest
from quality_checks.check_na import checkna
import pandas as pd

table_name = "sample"


class TestCheckNa(unittest.TestCase):
    def test_no_na_values(self):
        data = {"A": [1, 2, 3], "B": [4, 5, 6]}
        df = pd.DataFrame(data)

        result = checkna(df, table_name)

        self.assertFalse(
            result,
            "Expected the function to return False for DataFrame with no NaN values",
        )

    def test_single_column_with_na(self):
        data = {"A": [1, 2, 3], "B": [4, None, 6]}
        df = pd.DataFrame(data)

        result = checkna(df, table_name)

        self.assertTrue(
            result,
            "Expected the function to return True for DataFrame with NaN values in a column",
        )

    def test_multiple_columns_with_na(self):
        data = {"A": [1, None, 3], "B": [4, None, 6]}
        df = pd.DataFrame(data)

        result = checkna(df, table_name)

        self.assertTrue(
            result,
            "Expected the function to return True for DataFrame with NaN values in multiple columns",
        )

    def test_empty_dataframe(self):
        df = pd.DataFrame()

        result = checkna(df, table_name)

        self.assertFalse(
            result, "Expected the function to return False for an empty DataFrame"
        )
