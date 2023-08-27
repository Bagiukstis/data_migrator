import unittest
from quality_checks.check_dupes import checkdupes
import pandas as pd

table_name = "sample"


class TestCheckDupes(unittest.TestCase):
    def test_no_duplicates(self):
        data = {"A": [1, 2, 3], "B": [4, 5, 6]}
        df = pd.DataFrame(data)

        result = checkdupes(df, table_name)

        self.assertFalse(result, "Expected the function to return False")

    def test_duplicates_present(self):
        data = {"A": [1, 2, 3, 3], "B": [4, 5, 6, 6]}
        df = pd.DataFrame(data)

        result = checkdupes(df, table_name)

        self.assertTrue(result, "Expected the function to return True")

    def test_empty_dataframe(self):
        df = pd.DataFrame()

        result = checkdupes(df, table_name)

        self.assertFalse(
            result, "Expected the function to return False for an empty DataFrame"
        )
